class Directory:

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = []
        self.directories = {}

    def get_parent(self):
        return self.parent

    def add_directory(self, d):
        if not self.has_directory(d):
            self.directories[d] = Directory(str(d), self)

    def get_directory(self, d):
        return self.directories[d]
            
    def has_directory(self, d):
        return d in self.directories.keys()

    def add_file(self, file):
        if not self.has_file(file):
            self.files.append(file)

    def has_file(self, file):
        for f in self.files:
            if (f.name == file.name and f.size == file.size):
                return True
        return False

    def gather_all_under_given_size(self, size, dir_list):
        this_size = self.get_total_size()
        if (this_size <= size):
            dir_list.append(self)
        for key in self.directories.keys():
            self.directories[key].gather_all_under_given_size(size, dir_list)

    def gather_all_over_given_size(self, size, dir_list):
        this_size = self.get_total_size()
        if (this_size >= size):
            dir_list.append(self)
        for key in self.directories.keys():
            self.directories[key].gather_all_over_given_size(size, dir_list)

    def get_total_size(self):
        size = 0
        for f in self.files:
            size += f.size
        for key in self.directories.keys():
            size += self.directories[key].get_total_size()
        return size

    def print_self(self):
        print("--")
        print(self.name)
        for f in self.files:
            print (str(f.size) + " " + f.name)
        for key in self.directories.keys():
            print (self.directories[key].name)

        for key in self.directories.keys():
            print (self.directories[key].print_self())


class File:

    def __init__(self, name, size):
        self.name = name
        self.size = size
