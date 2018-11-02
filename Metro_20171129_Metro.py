import tkinter as tk

line1 = ["Dupont", "Spadina", "St George", "Museum", "Wellesley", "Bloor Yonge", "Lonsdale", "York's Mills",
         "Sheppard Younge", "North York Center"]
line2 = ["Bathurst", "Spadina", "St George", "Bay", "Bloor Yonge", "Shelbourne", "Kennedy"]
line3 = ["Kennedy", "McCowan"]
line4 = ["Sheppard Younge", "Don Mills"]

lines = [line1, line2, line3, line4]


def create_all_lines(lines):
    """
    Function that creates a single list of all the stations contained in a 2D lists of stations
    :param lines: 2D list of stations
    :return: list of all the stations contained in lines
    """
    all_lines = []
    for line in lines:
        for station in line:
            all_lines.append(station)
    return all_lines


def create_connections(all_lines):
    """
    Function that creates a list of all the stations that have connections with multiple lines
    :param all_lines: list of all the stations
    :return: list of stations that have connections with multiple lines
    """
    connections = []
    for station in all_lines:
        if all_lines.count(station) > 1:
            connections.append(station)
    return connections


def create_graph(lines):
    """
    Function that creates a dict given 2D lists of stations
    :param lines: 2D list of stations
    :return: dict of stations with their neighbors as lists
    """
    graph = {}
    for line in lines:
        for station in range(len(line)):
            if line[station] not in graph:
                graph[line[station]] = []
            if station == 0 and line[station + 1] not in graph[line[station]]:
                graph[line[station]].append(line[station + 1])
            elif station == len(line) - 1 and line[station - 1] not in graph[line[station]]:
                graph[line[station]].append(line[station - 1])
            else:
                if line[station - 1] not in graph[line[station]]:
                    graph[line[station]].append(line[station - 1])
                if line[station + 1] not in graph[line[station]]:
                    graph[line[station]].append(line[station + 1])
            if len(graph[line[station]]) > 2 and line[station] not in connections:
                connections.append(line[station])
    return graph


def create_station_line(all_lines):
    """
    Function that create a dict of stations with their respective lines
    :param all_lines: list of all the stations
    :return: dict of station as keys and lines as values
    """
    station_line = {}
    for line in range(len(all_lines)):
        for station in lines[line]:
            if station not in station_line:
                station_line[station] = []
            station_line[station].append(line+1)
    return station_line


all_stations = create_all_lines(lines)
connections = sorted(set(create_connections(all_stations)))
all_stations = sorted(set(all_stations))
graph = create_graph(lines)
station_line = create_station_line(lines)


def display(graph):
    for element in graph:
        print(element, "\t", str(graph[element]))


class First_Page(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        # Set padx & pady
        self.get_padx = 0
        self.get_pady = 0

        # BUTTON FROM
        self.start = tk.Button(master, text="From".upper(), justify="center", wraplength=90,
                               command=lambda: self.open_second("From"))
        self.start.grid(row=1, column=0, padx=self.get_padx, pady=self.get_pady)
        self.start.config(height=3, width=20)

        # LABEL FROM
        self.var_start = tk.StringVar()
        self.label_start = tk.Label(master, textvariable=self.var_start, justify="center", wraplength=90)
        self.label_start.grid(row=1, column=1, padx=self.get_padx, pady=self.get_pady)
        self.label_start.config(height=3, width=20)

        # BUTTON TO
        self.to = tk.Button(master, text="To".upper(), justify="center", wraplength=90,
                               command=lambda: self.open_second("To"))
        self.to.grid(row=2, column=0, padx=self.get_padx, pady=self.get_pady)
        self.to.config(height=3, width=20)

        # LABEL TO
        self.var_to = tk.StringVar()
        self.label_to = tk.Label(master, textvariable=self.var_to, justify="center", wraplength=90)
        self.label_to.grid(row=2, column=1, padx=self.get_padx, pady=self.get_pady)
        self.label_to.config(height=3, width=20)

        # PATH
        self.path = tk.StringVar()
        self.label_path = tk.Label(master, textvariable=self.path, justify="center", wraplength=90)
        self.label_path.grid(row=3, column=0, padx=self.get_padx, pady=self.get_pady, columnspan=2)
        self.label_path.config(height=7, width=40)

        # VALIDATE
        self.validate = tk.Button(master, text="Validate".upper(), justify="center", wraplength=90,
                                  command=lambda: self.BFS(graph, self.var_start.get(), self.var_to.get()))
        self.validate.grid(row=4, column=0, padx=self.get_padx, pady=self.get_pady, columnspan=2)
        self.validate.config(height=3, width=40)

    def open_second(self, state):
        self.second_win = tk.Toplevel(self)
        self.second_win.wm_title("Please select line".upper())

        # Specify starting row and column for items
        self.start = [-1, 1]

        # BACK TO MENU
        self.back_menu = tk.Button(self.second_win, text="< Back to menu".upper(), justify="center", wraplength=90,
                                   command=self.second_win.destroy)
        self.back_menu.grid(row=0, column=0, padx=self.get_padx, pady=self.get_pady)
        self.back_menu.config(height=3, width=20)

        # LINE 01
        self.line1 = tk.Button(self.second_win, text="Line 01".upper(), justify="center", wraplength=90,
                               command=lambda: self.open_third(line1, "Line 01".upper(), state))
        self.line1.grid(row=1, column=0, padx=self.get_padx, pady=self.get_pady)
        self.line1.config(height=3, width=20)

        # LINE 02
        self.line2 = tk.Button(self.second_win, text="Line 02".upper(), justify="center", wraplength=90,
                               command=lambda: self.open_third(line2, "Line 02".upper(), state))
        self.line2.grid(row=1, column=1, padx=self.get_padx, pady=self.get_pady)
        self.line2.config(height=3, width=20)

        # LINE 03
        self.line3 = tk.Button(self.second_win, text="Line 03".upper(), justify="center", wraplength=90,
                               command=lambda: self.open_third(line3, "Line 03".upper(), state))
        self.line3.grid(row=2, column=0, padx=self.get_padx, pady=self.get_pady)
        self.line3.config(height=3, width=20)

        # LINE 04
        self.line4 = tk.Button(self.second_win, text="Line 04".upper(), justify="center", wraplength=90,
                               command=lambda: self.open_third(line4, "Line 04".upper(), state))
        self.line4.grid(row=2, column=1, padx=self.get_padx, pady=self.get_pady)
        self.line4.config(height=3, width=20)

        # ALL LINE
        self.all_stations = tk.Button(self.second_win, text="All stations".upper(), justify="center", wraplength=90,
                                      command=lambda: self.open_third(all_stations, "All stations".upper(), state))
        self.all_stations.grid(row=3, column=0, padx=self.get_padx, pady=self.get_pady, columnspan=2)
        self.all_stations.config(height=3, width=40)

    def open_third(self, line, name, state):
        """
        Create a button for each stations in line
        :param line: list of station in line
        :param name: string, name of line
        """
        third_win = tk.Toplevel(self)
        third_win.wm_title(name.upper())

        # BACK TO LINES
        self.back_menu_third = tk.Button(third_win, text="< Back to lines".upper(), justify="center", wraplength=90,
                                         command=third_win.destroy)
        self.back_menu_third.grid(row=0, column=0, padx=self.get_padx,
                                  pady=self.get_pady)
        self.back_menu_third.config(height=3, width=20)

        third_win.start = [0, 0]

        def select(station):
            if state == "From":
                self.var_start.set(station)
            else:
                self.var_to.set(station)
            third_win.destroy()
            self.second_win.destroy()

        for items in sorted(line):
            third_win.start[0] += 1
            if third_win.start[0] % 6 == 0:
                third_win.start[0] = 1
                third_win.start[1] += 1
            third_win.station = tk.Button(third_win, text=items.upper(), wraplength=90,
                                          command=lambda current_station=items: select(current_station))
            third_win.station.grid(row=third_win.start[0], column=third_win.start[1])
            third_win.station.config(height=3, width=20)

    def BFS(self, graph, start, end):
        """
        Given a graph, a starting and destination point, return path from start to destination
        :param graph: dict of adjacent stations
        :param start: string, name of starting point
        :param end: string, name of destination
        :return: list of stations between starting point and destination 
        """
        level = {start: 0}
        parent = {start: None}
        i = 1
        frontier = [start]
        while frontier:
            nextous = []
            for station in frontier:
                for adj in graph[station]:
                    if adj not in level:
                        level[adj] = i
                        parent[adj] = station
                        nextous.append(adj)
                    if adj.lower() == end.lower():
                        rewind = adj
                        path = []
                        while rewind.lower() != start.lower():
                            path.append(rewind)
                            rewind = parent[rewind]
                        path.append(start)
                        self.path.set(path[::-1])

            frontier = nextous
            i += 1


    def find_line(self, station):
        """
        Function that return the line passing through station
        :param station: string, station tested
        :return: list of lines passing through station
        """
        return station_line[station]

    def intersect(self, a, b):
        return list(set(a) & set(b))

    def path_finder(self, path):
        """
        Function that returns lines to take and connections
        :param path: list of stations between starting point and destination
        :return: list of lines to take and connections
        """
        if len(self.intersect(self.find_line(path[0]), self.find_line(path[len(path)-1]))) == 1:
            self.path.set(self.find_line(path[0]))
        else:
            self.path.set("NOOOPE")



root = tk.Tk()
root.wm_title("Metro Trip".upper())
app = First_Page(master=root)
app.mainloop()
