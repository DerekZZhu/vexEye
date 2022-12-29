class Comp:
    def __init__(self, name, eligible, viab, judging, link, dates, participants):
        self.name = name
        self.eligible = eligible
        self.viability = viab
        self.judging = judging
        self.link = link
        self.dates = dates
        self.participants = participants

    def toDict(self):
        return {
            "name":self.name,
            "eligibility":self.eligible,
            "viability":self.viability,
            "judging":self.judging,
            "link":self.link,
            "dates":self.dates,
            "participants":self.participants
        }