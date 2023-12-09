class Job:
  def __init__(self, maJob, tenJob, tenNganh, tienLuong):
    self._maJob = maJob
    self._tenJob = tenJob
    self._tenNganh = tenNganh
    self._tienLuong = tienLuong

  def getMaJob(self):
    return self._maJob

  def getTenJob(self):
    return self._tenJob

  def getTenNganh(self):
    return self._tenNganh

  def getTienLuong(self):
    return self._tienLuong

  def setMaJob(self, majob):
    self._maJob = majob

  def setTenJob(self, tenjob):
    self._tenJob = tenjob

  def setTenNganh(self, tennganh):
    self._tenNganh = tennganh

  def setTienLuong(self, tienluong):
       self._tienLuong = tienluong

class AI(Job):
  def __init__(self, maJob, tenJob, tenNganh, tienLuong, Py_Skill, ML_Skill, DL_Skill, Math_Skill):
    super().__init__( maJob, tenJob, tenNganh, tienLuong)
    self.Py_Skill = Py_Skill
    self.ML_Skill = ML_Skill
    self.DL_Skill = DL_Skill
    self.Math_Skill = Math_Skill

  def evaluate(self):
    if (self.Py_Skill + self.ML_Skill + self.DL_Skill + self.Math_Skill) / 4 > 9.0:
      print("Rat phu hop")
    elif (self.Py_Skill + self.ML_Skill + self.DL_Skill + self.Math_Skill) / 4 > 7.0:
      print("Phu hop")
    elif (self.Py_Skill + self.ML_Skill + self.DL_Skill + self.Math_Skill) / 4 > 5.0:
      print("Tam Duoc")
    elif (self.Py_Skill + self.ML_Skill + self.DL_Skill + self.Math_Skill) / 4 > 3.0:
      print("Can bo sung them kien thuc")
      if self.Py_Skill < 4.0:
        print("Python skill")
      if self.ML_Skill < 4.0:
        print("ML Skill")
      if self.DL_Skill < 4.0:
           print("Math Skill")
    else:
        print("Can hoc lai kien thuc base")

  def __str__(self):
    return f"{self.getMaJob()} || {self.getTenJob()} || {self.getTenNganh()} || {self.getTienLuong()} || {self.Py_Skill} || {self.ML_Skill} || {self.DL_Skill} || {self.Math_Skill}"



class Backend(Job):
  def __init__(self, maJob, tenJob, tenNganh, tienLuong, SQL_Skill, OOP_Skill, Api_Skill, Java_Skill):
    Job.__init__(self, maJob, tenJob, tenNganh, tienLuong)
    self.SQL_Skill = SQL_Skill
    self.OOP_Skill = OOP_Skill
    self.Api_Skill = Api_Skill
    self.Java_Skill = Java_Skill

  def evaluate(self):
    if (self.SQL_Skill + self.OOP_Skill + self.Api_Skill + self.Java_Skill) / 4 > 9.0:
      print("Rất phù hợp")
    elif (self.SQL_Skill + self.OOP_Skill + self.Api_Skill + self.Java_Skill) / 4 > 7.0:
      print("Phù hợp")
    elif (self.SQL_Skill + self.OOP_Skill + self.Api_Skill + self.Java_Skill) / 4 > 5.0:
      print("Tạm được")
    elif (self.SQL_Skill + self.OOP_Skill + self.Api_Skill + self.Java_Skill) / 4 > 3.0:
      print("Cần bổ sung thêm kiến thức: ")
      if self.SQL_Skill < 4.0:
        print("SQL_Skill")
      if self.OOP_Skill < 4.0:
        print("OOP_Skill")
      if self.Api_Skill < 4.0:
        print("Api_Skill")
      if self.Java_Skill < 4.0:
          print("Java_Skill")
    else:
          print("Cần học lại kiến thức base")
  def __str__(self):
    return f"{self.getMaJob()} || {self.getTenJob()} || {self.getTenNganh()} || {self.getTienLuong()} || {self.SQL_Skill} || {self.OOP_Skill} || {self.Api_Skill} || {self.Java_Skill}"


class Frontend(Job):
  def __init__(self, maJob, tenJob, tenNganh, tienLuong, Html_Skill, Css_Skill, Nodejs_Skill, UX_Skill, UI_Skill):
        Job.__init__(self, maJob, tenJob, tenNganh, tienLuong)
        self.Html_Skill = Html_Skill
        self.Css_Skill = Css_Skill
        self.Nodejs_Skill = Nodejs_Skill
        self.UX_Skill = UX_Skill
        self.UI_Skill = UI_Skill
  def evaluate(self):
    if (self.Html_Skill + self.Css_Skill + self.Nodejs_Skill + self.UX_Skill + self.UI_Skill) / 5> 9.0:
      print("Rất phù hợp")
    elif (self.Html_Skill + self.Css_Skill + self.Nodejs_Skill + self.UX_Skill + self.UI_Skill) / 5 > 7.0:
      print("Phù hợp")
    elif (self.Html_Skill + self.Css_Skill + self.Nodejs_Skill + self.UX_Skill + self.UI_Skill) / 5 > 5.0:
      print("Tạm được")
    elif (self.Html_Skill + self.Css_Skill + self.Nodejs_Skill + self.UX_Skill + self.UI_Skill) / 5 > 3.0:
      print("Cần bổ sung thêm kiến thức: ")
      if self.Html_Skill < 4.0:
        print("Html_Skill")
      if self.Css_Skill < 4.0:
        print("Css_Skill")
      if self.Nodejs_Skill < 4.0:
          print("Nodejs_Skill")
      if self.UX_Skill < 4.0:
          print("UX_Skill")
      if self.UI_Skill < 4.0:
          print("UI_Skill")
    else:
      print("Cần học lại kiến thức base")
  def __str__(self):
    return f"{self.getMaJob()} || {self.getTenJob()} || {self.getTenNganh()} || {self.getTienLuong()} || {self.Html_Skill} || {self.Css_Skill} || {self.Nodejs_Skill} || {self.UX_Skill} || {self.UI_Skill}"


class Fullstack(Backend, Frontend):
    def __init__(self, maJob, tenJob, tenNganh, tienLuong,
                 SQL_Skill, OOP_Skill, Api_Skill, Java_Skill,
                 Html_Skill, Css_Skill, Nodejs_Skill, UX_Skill, UI_Skill):
        Backend.__init__( self, maJob, tenJob, tenNganh, tienLuong, SQL_Skill, OOP_Skill, Api_Skill, Java_Skill)
        Frontend.__init__( self, maJob, tenJob, tenNganh, tienLuong, Html_Skill, Css_Skill, Nodejs_Skill, UX_Skill, UI_Skill)

    def evaluate(self):
        average_fullstack_skill = (self.SQL_Skill + self.OOP_Skill + self.Api_Skill + self.Java_Skill + self.Html_Skill + self.Css_Skill + self.Nodejs_Skill + self.UX_Skill + self.UI_Skill) / 9

        if average_fullstack_skill > 9.0:
            print("Rất phù hợp")
        elif average_fullstack_skill > 7.0:
            print("Phù hợp")
        elif average_fullstack_skill > 5.0:
            print("Tạm được")
        elif average_fullstack_skill > 3.0:
            print("Cần bổ sung thêm kiến thức: ")
            if Backend.SQL_Skill < 4.0:
                print("SQL_Skill")
            if Backend.OOP_Skill < 4.0:
                print("OOP_Skill")
            if Backend.Api_Skill < 4.0:
                print("Api_Skill")
            if Backend.Java_Skill < 4.0:
                print("Java_Skill")
            if Frontend.Html_Skill < 4.0:
                print("Html_Skill")
            if Frontend.Css_Skill < 4.0:
                print("Css_Skill")
            if Frontend.Nodejs_Skill < 4.0:
                print("Nodejs_Skill")
            if Frontend.UX_Skill < 4.0:
                print("UX_Skill")
            if Frontend.UI_Skill < 4.0:
                print("UI_Skill")
        else:
            print("Cần học lại kiến thức base")
    def __str__(self):
      return f"{self.getMaJob()} || {self.getTenJob()} || {self.getTenNganh()} || {self.getTienLuong()} ||{self.SQL_Skill} || {self.OOP_Skill} || {self.Api_Skill} || {self.Java_Skill} || {self.Html_Skill} || {self.Css_Skill} || {self.Nodejs_Skill} || {self.UX_Skill} || {self.UI_Skill}"

def main():
    # AI
    ai = AI(
        maJob="AI001",
        tenJob="Kỹ sư trí tuệ nhân tạo",
        tenNganh="Công nghệ thông tin",
        tienLuong=20000000,
        Py_Skill=0,
        ML_Skill=2,
        DL_Skill=3,
        Math_Skill=1,
    )
    # Frontend
    frontend = Frontend(
        maJob="FE001",
        tenJob="Kỹ sư phát triển Frontend",
        tenNganh="Công nghệ thông tin",
        tienLuong=15000000,
        Html_Skill=5,
        Css_Skill=5,
        Nodejs_Skill=5,
        UX_Skill=4,
        UI_Skill=6.5,
    )

    # Backend
    backend = Backend(
        maJob="BE001",
        tenJob="Kỹ sư phát triển Backend",
        tenNganh="Công nghệ thông tin",
        tienLuong=18000000,
        SQL_Skill=3,
        OOP_Skill=4,
        Api_Skill=5,
        Java_Skill=3.5,
    )

    # Fullstack
    fullstack = Fullstack(
        maJob="FS001",
        tenJob="Kỹ sư Fullstack",
        tenNganh="Công nghệ thông tin",
        tienLuong=22000000,
        SQL_Skill=9.0,
        OOP_Skill=9.5,
        Api_Skill=9.0,
        Java_Skill=9.0,
        Html_Skill=9.0,
        Css_Skill=9.5,
        Nodejs_Skill=9.0,
        UX_Skill=9.0,
        UI_Skill=9.0,
    )

    print("**Thông tin và đánh giá của đối tượng AI**")
    print(ai)
    ai.evaluate()
    print("\n**Thông tin và đánh giá của đối tượng Frontend**")
    print(frontend)
    frontend.evaluate()

    print("\n**Thông tin và đánh giá của đối tượng Backend**")
    print(backend)
    Backend.evaluate(backend)

    print("\n**Thông tin và đánh giá của đối tượng Fullstack**")
    print(fullstack)
    fullstack.evaluate()

if __name__ =="__main__":
  main()