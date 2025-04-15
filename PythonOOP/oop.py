# Quetsion1
# class of a tech student and child class of womenintech
class TechStudent:
    def __init__(self, name, university, year, skills):
        self.name = name
        self.university = university
        self.year = year
        self.skills = skills if skills else []
    # intro method
    def introduction(self):
        return f"Hi👋, I am {self.name}, a student at {self.university} currently in year {self.year}."
    # Skills method
    def skills_learnt(self, skill):
        self.skills.append(skill)
        return f"{self.name}'s current skills: {', '.join(self.skills)}"
    
# Child class womeninTech
class womaninTech(TechStudent):
    def __init__(self, name, university, year, skills=None, mentees=None, initiatives=None):
        super().__init__(name, university, year, skills)
        self.mentees = mentees if mentees else []
        self.initiatives = initiatives if mentees else []
    
    # Mentor method
    def mentor(self, mentee_name):
        self.mentees.append(mentee_name)
        return f"{self.name} is now metoring {mentee_name}!"
    # initiatives method by the womaninTech
    def start_initiative(self, initiative_name):
        self.initiatives.append(initiative_name)
        return f"{self.name} has started the {initiative_name} initiative which is a major milestone for women in Tech!"
    def profile_summary(self):
        return (
            f"{self.introduction()}\n"
            f"Skills: {', '.join(self.skills)}\n"
            f"Mentees: {', '.join(self.mentees)}\n"
            f"Initiatives: {', '.join(self.initiatives)}\n"
        )
    
# Instantiation step
student = womaninTech("Tabitha", "Africa International University", 4)
print(student.introduction)
print(student.skills_learnt("Python OOP"))
print(student.skills_learnt("Python Libraries"))
print(student.mentor("@Nangani"))
print(student.start_initiative("Code Like a Girl.Build Like a Pro"))
print(student.profile_summary())