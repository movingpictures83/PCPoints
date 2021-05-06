import PyPluMA

class PCPointsPlugin:
   def input(self, filename):
      self.parameters = dict()
      paramfile = open(filename, 'r')
      for line in paramfile:
         contents = line.split('\t')
         self.parameters[contents[0]] = contents[1].strip()

      self.infile = open(PyPluMA.prefix()+"/"+self.parameters["infile"], 'r')
      self.mapfile = open(PyPluMA.prefix()+"/"+self.parameters["mapping"], 'r')
      self.mapfile.readline()
      self.group = self.parameters["group"]

   def run(self):
      self.samples = []
      for line in self.mapfile:
         contents = line.strip().split('\t')
         if (contents[3] == self.group):
            self.samples.append(contents[0])

   def output(self, filename):
      outfile = open(filename, 'w')
      #firstline = infile.readline()
      #header = firstline.split('\t')
      x = []
      y = []
      z = []
      for line in self.infile:
         contents = line.strip().split('\t')
         if (contents[0] in self.samples):
              outfile.write(contents[1]+"\t"+contents[2]+"\n")
