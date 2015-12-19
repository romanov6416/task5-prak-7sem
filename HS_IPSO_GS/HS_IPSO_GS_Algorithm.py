import random
import copy

from Common.Algorithm import Algorithm
from Common.Module import Module, NONE, NVP01, NVP11, RB11
from Common.System import System


class HS_IPSO_GS_Algorithm(Algorithm):
    def __init__(self):
        Algorithm.__init__(self)
        self.population = list()
        self._iter_count_without_change = 0
        # begin with first step
        self.__step = 1
        self.__step_algo = {1: "HS", 2: "IPSO", 3: "GS", 4: "END"}
        self.currentSolution = None
        # self.upper_pos = [len(module.sw) - 1 for module in Module.conf.modules]
        # self.lower_pos = [0] * Module.conf.modNum

    def Step(self):
        """
        proccess algorithm step.
        return True, if algorithm is finished, else False
        :return: bool
        """
        # change step
        if self.__step == 1 and self._iter_count_without_change >= self.algconf.m1:
            # HS algo solution is init value for each particle in population IPSO
            self.population = [Particle(initial_system=self.currentSolution)
                               for s in self.population]
            self.Update()
            self.__step += 1
        elif self.__step == 2 and self._iter_count_without_change >= self.algconf.m2:
            self.__step += 1
        elif self.__step == 3 and self._iter_count_without_change > 0:
            self.__step += 1
            return True

        # execute step of algorithm according to __step
        if self.__step == 1:
            self._hs_algorithm()
        elif self.__step == 2:
            self._ipso_algorithm()
        else:
            self._gs_algorithm()
        # update system variables
        self.Update()
        self.currentIter += 1
        return self.__step == 4

    def Run(self):
        random.seed()
        # init population
        self.population = [Particle() for i in xrange(self.algconf.ps)]
        self.Update()

        # in cycle execute algorithm
        while self.currentIter < self.algconf.k:
            if self.Step():
                break
            print "%s) Algo = '%s' Rel = %s Cost = %s (best is not changed %s)" % (
                self.currentIter, self.__step_algo[self.__step],
                self.currentSolution.rel if self.currentSolution else None,
                self.currentSolution.cost if self.currentSolution else None,
                self._iter_count_without_change)
        print "----------------------------------------------------------------------------\n"
        if self.currentSolution:
            print "Best solution: {reliable: %s, cost: %s}" % (self.currentSolution.rel,
                                                               self.currentSolution.cost)
        else:
            print "Solution is not found"

    def Clear(self):
        Algorithm.Clear(self)
        self.population = list()
        self._iter_count_without_change = 0
        # begin with first step
        self.__step = 1

    def _hs_algorithm(self):
        """
        apply HS algorithm
        :return: None
        """
        for particle in self.population:
            sys = particle.system
            for module in particle.system.modules:
                d = module.num
                ran = random.random()
                if ran < self.algconf.hmcr:
                    if ran < self.algconf.par:
                        continue
                    else:
                        module.chosen_sw += 2 * (ran - 0.5) * self.algconf.bw
                else:
                    # sw_number E [x'; x''], where x' == 0, x'' == <number of sw>
                    module.chosen_sw += ran * (sys.modules[d].sw_num - 1)

    def _ipso_algorithm(self):
        """
        apply IPSO algorithm
        :return: None
        """
        for i in xrange(len(self.population)):
            particle = self.population[i]
            for module in particle.system.modules:
                if particle.best_solution is None:
                    # bad solution => create new particle
                    self.population[i] = Particle()
                    continue
                d = module.num
                ran = random.random()
                if ran < ((1 - self.currentIter / self.algconf.k) ** 0.5):
                    module.chosen_sw += 2 * ran * (particle.best_solution.modules[d].chosen_sw -
                                                   module.chosen_sw)
                else:
                    module.chosen_sw += 2 * ran * (self.currentSolution.modules[d].chosen_sw -
                                                   module.chosen_sw)

    def _gs_algorithm(self):
        """
        apply Golden Search algorithm
        return True if best solution is changed else False
        :return: bool
        """
        if self.currentSolution is None:
            return
        TOP_DEVIATION_COUNT = 5
        delta1_list = [self.algconf.delta1 * (self.algconf.t ** i)
                       for i in xrange(self.algconf.t_max)]

        pairs_list = [(module.num, self.__get_std_deviation(module.num))
                      for module in Module.conf.modules]
        pairs_list.sort(key=lambda pair: pair[1], reverse=True)

        # get TOP_DEVIATION_COUNT modules with first top standard deviations
        top_module_numbers_list = [module_info[0] for module_info in
                                   pairs_list[:TOP_DEVIATION_COUNT]]
        mod_num_pairs_list = [(n1, n2) for n1 in top_module_numbers_list
                              for n2 in top_module_numbers_list if n1 != n2]
        self.population = [Particle(self.currentSolution) for i in mod_num_pairs_list]
        for i in xrange(len(mod_num_pairs_list)):
            p = self.population[i] # short name of particle
            # n1, n2 - system module numbers
            n1, n2 = mod_num_pairs_list[i]
            p.system.modules[n2].chosen_sw += ((random.random() - 0.5) * GoldenSearch(
                p.system.get_new_rel, n2).compute(0, self.algconf.delta2))
            p.system.modules[n1].chosen_sw += delta1_list[int((random.random() - 0.5) *
                                                              2 * (len(delta1_list) - 1))]
        self.Update()

    def Update(self):
        """
        update currentSolution according to population
        :return: None
        """
        self._iter_count_without_change += 1
        for particle in self.population:
            particle.Update()
            if particle.best_solution is not None and (self.currentSolution is None or
                                                       self.currentSolution.rel < particle.best_solution.rel):
                self.currentSolution = copy.deepcopy(particle.best_solution)
                self._iter_count_without_change = 0
        # # debug
        print "BEST_SOLUTION: {%s: %s}" % (self.currentSolution.rel if self.currentSolution else None,
                                           self.currentSolution.cost if self.currentSolution else None,)
        print ["CURRENT: %s; BEST: %s" % ({particle.system.rel: particle.system.cost},
                                          {particle.best_solution.rel: particle.best_solution.cost}
                                          if particle.best_solution else {None: None})
               for particle in self.population]
        print "======================================================================="
        # for particle in self.population:
        #     print "{%s: %s} %s:" % (
        #         particle.system.rel, particle.system.cost,
        #         [(m.chosen_sw, m.rel, m.cost) for m in particle.system.modules],
        #     )

    def __get_std_deviation(self, module_number):
        module = Module.conf.modules[module_number]
        reliable_list = [e.rel for e in module.sw]
        # get average (arithmetical mean)
        average = reduce(lambda s, x: s + x, reliable_list, 0) / len(module.sw)
        # return standard deviation
        return reduce(lambda s, x: s + (x - average) ** 2, reliable_list, 0) / len(module.sw)

    def __apply_best(self):
        for partical in self.population:
            partical.cur_pos = self.currentSolution.cur_pos


class Particle(object):
    def __init__(self, initial_system=None):
        self.system = copy.deepcopy(initial_system) if initial_system else SystemAlgo()
        self.best_solution = None
        self.Update()

    def Update(self):
        self.system.Update()
        # print self.system.cost
        if self.system.CheckConstraints() and (self.best_solution is None or
                                               self.best_solution.rel < self.system.rel):
            # print "update best, cost == %s" % self.system.cost
            self.best_solution = copy.deepcopy(self.system)


class SystemAlgo(System):
    def __init__(self):
        """

        :param algorithm:
        :return:
        """
        # self.algorithm = algorithm
        self.modules = [ModuleAlgo(i) for i in xrange(Module.conf.modNum)]
        self.mod_num = len(self.modules)

    def Update(self, use_metamodel=False, add=False):
        """
        update reliable and cost in modules
        according to self.cur_pos

        :param use_metamodel: bool  don't use
        :param add: bool    don't use
        :return: None
        """
        self.rel = 1.0
        self.cost = 0
        for module in self.modules:
            module.Update()
            self.rel *= module.rel
            self.cost += module.cost

    def CheckConstraints(self):
        """
        Checks cost constraints.
        :return: bool
        """
        ok = True
        # hack just for cost checking
        for c in [c for c in self.constraints if c.__class__.__name__ == "CostConstraints"]:
            ok = c.CheckConstraints(self)
            if not ok:
                break
        return ok

    def get_new_rel(self, module_number, new_chosen):
        self.modules[module_number].chosen_sw = new_chosen
        self.Update()
        return self.rel


class ModuleAlgo(object):
    def __init__(self, number, sw_number=None):
        self.num = number
        # init., choses cheapest sw
        self.sw_num = len(Module.conf.modules[self.num].sw)
        self.chosen_sw = random.uniform(0, self.sw_num - 1)
        self.cur_sw = -1
        self.cost = -1
        self.rel = -1

    def Update(self):
        self.correct_chosen_sw()
        self.cur_sw = int(round(self.chosen_sw))
        self.cost = Module.conf.modules[self.num].sw[self.cur_sw].cost
        self.rel = Module.conf.modules[self.num].sw[self.cur_sw].rel

    def correct_chosen_sw(self):
        if self.chosen_sw > len(Module.conf.modules[self.num].sw) - 1:
            self.chosen_sw = len(Module.conf.modules[self.num].sw) - 1
        elif self.chosen_sw < 0:
            self.chosen_sw = 0

    # @staticmethod
    # def get_cheapest_sw_number(module_number):
    #     chosen_sw_number = 0
    #     for sw_number in xrange(len(Module.conf.modules[module_number].sw)):
    #         if (ModuleAlgo.get_sw(chosen_sw_number, sw_number).cost >
    #                 ModuleAlgo.get_sw(module_number, sw_number).cost):
    #             chosen_sw_number = sw_number
    #     return chosen_sw_number

    @staticmethod
    def get_sw(module_number, sw_number):
        return Module.conf.modules[module_number].sw[sw_number]
    #
    # @staticmethod
    # def sw_number(module_number):
    #     return len(Module.conf.modules[module_number].sw)


class GoldenSearch(object):
    def __init__(self, function, component_number):
        self.func = lambda x: function(component_number, x)
        self.accuracy = 0.1
        self.fi = (1 + 5 ** 0.5) / 2

    def compute(self, interval_start, interval_end, maximum=True):
        a = interval_start
        b = interval_end
        f = self.func

        x1 = b - (b - a) / self.fi
        x2 = a + (b - a) / self.fi
        while (b - a) > self.accuracy:
            if self.__condition(f(x1), f(x2), maximum):
                a = x1
                x1 = x2
                x2 = a + (b - a) / self.fi
            else:
                b = x2
                x2 = x1
                x1 = b - (b - a) / self.fi
        return (a + b) / 2

    @staticmethod
    def __condition(value1, value2, maximum):
        if maximum:
            return value1 <= value2
        else:
            return value1 >= value2

