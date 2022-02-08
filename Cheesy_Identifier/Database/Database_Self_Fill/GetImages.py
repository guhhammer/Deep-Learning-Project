
import os, time, math


# query = [ ["name", "no pakage ...."], ...]

class extractor():
    def __init__(self, _path_, _queries_, _n_images_, wait_time=125, for_loop_step=4, _max_extracted_=200, _clean_="yes"):
        self.xampp_path, self.query, self.number, self.clean = _path_, _queries_, _n_images_, _clean_
        self.wait_time, self.number_of_simultaneous_processes = wait_time, for_loop_step
        self.max = _max_extracted_ if _max_extracted_ < 200 else 200

    def to_queries(self):
        ret = []
        for x in self.query:
            if x[1] == "":
                ret.append(["_".join(x[0].split()), "_".join(x[0].split())])
                continue
            ret.append(["_".join(x[0].split()), "_".join(x[0].split())+"_"+"_".join(x[1].split())])
        return ret

    def fragment_query(self, query):
        i, steps, ret = 0, (self.number / self.max), []

        exceed = math.ceil(steps)
        while i <= steps:
            start_at, until = i*self.max, (i+1)*self.max if (i+1) < exceed else self.number
            ret.append(
                (
                 "?link="+query[0]+"_BR_"+query[1]+"_BR_"+str(start_at)+"_BR_"+str(until)+"_BR_"+
                 self.clean+"_BR_"+"\\".join(os.path.abspath(os.getcwd()).split("\\")[:-1])
                )
            )
            if self.clean == "yes":
                self.clean = "no"
            i += 1
        return ret

    def fragment_array(self):
        return [ self.fragment_query(query) for query in self.to_queries() ]

    def cmd_command(self, link):
        return "start /max http://localhost/Extractor_algorithm_Cheesy_Identifier/getImages.php"+link

    def start_apache(self, sleep_time=5):
        os.system("START \"\" "+self.xampp_path+"/apache_start")
        time.sleep(sleep_time)

    def stop_apache(self, sleep_time=4):
        time.sleep(sleep_time)
        os.system("START \"\" "+self.xampp_path+"/apache_stop")

    def thread_start(self):
        self.query = self.fragment_array()
        for x in range(0, len(self.query), self.number_of_simultaneous_processes):
            i = 0
            while i < len(self.query[x]):

                if x+self.number_of_simultaneous_processes < len(self.query):
                    for j in range(x, x+self.number_of_simultaneous_processes):
                        os.system(self.cmd_command(self.query[j][i]))
                else:
                    for j in range(x, len(self.query)):
                        os.system(self.cmd_command(self.query[j][i]))

                time.sleep(self.wait_time)
                i += 1

    def start(self):
        self.start_apache()
        self.thread_start()
        self.stop_apache()

