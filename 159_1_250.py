# SRM 159
# DIV 1
# 300
# 136.45 awarded
# was thoughtful in solution. only complied & tested once. got it on first try

class FryingHamburgers():
    def howLong(self, panSize, hamburgers):
        m = hamburgers
        n = panSize
        time = 0
        cleanCycles = (m / n) - 1
        if m > n and cleanCycles > 0:
            time += 10*cleanCycles
            time += 15
        elif m > n and cleanCycles == 0:
            time += 15
        elif m <= n and m > 0:
            time += 10
            
        return time