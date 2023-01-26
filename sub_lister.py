import requests
import colorama
import optparse

f = colorama.Fore
green = f.GREEN
red = f.RED
yellow = f.YELLOW
cyan = f.CYAN

class SubLister:
    def __init__(self):

        banner = '''
                            $$\             $$\ $$\           $$$$$$$$\                   
                            $$ |            $$ |\__|          \____$$  |                  
        $$$$$$$\ $$\   $$\ $$$$$$$\        $$ |$$\  $$$$$$$\     $$  /$$$$$$\   $$$$$$\  
        $$  _____|$$ |  $$ |$$  __$$\       $$ |$$ |$$  _____|   $$  /$$  __$$\ $$  __$$\ 
        \$$$$$$\  $$ |  $$ |$$ |  $$ |      $$ |$$ |\$$$$$$\    $$  / $$$$$$$$ |$$ |  \__|
        \____$$\ $$ |  $$ |$$ |  $$ |      $$ |$$ | \____$$\  $$  /  $$   ____|$$ |      
        $$$$$$$  |\$$$$$$  |$$$$$$$  |      $$ |$$ |$$$$$$$  |$$  /   \$$$$$$$\ $$ |      
        \_______/  \______/ \_______/$$$$$$\\__|\__|\_______/ \__/     \_______|\__|      
                                    \______|                                                                                
        '''
        print(red, banner)
        print(cyan, "\t[*] By Casanova ;)")
        print(red, 90*"=")

    def get_args(self):
        parser = optparse.OptionParser()
        parser.add_option("-d", "--domain", dest="url", help="Target domain to map")
        parser.add_option("-w", "--wordlist", dest="list", help="Wordlist to use")
        parser.add_option("-o", "--outfile", dest="outputfile", help="File to use for saving the output.")
        parser.add_option("-t", "--timeout", dest="timeout", help="Total number of seconds before quiting connection (default : 2)")
        self.options, args = parser.parse_args()

        if not self.options.url:
            parser.error("[-] Please provide a domain.")
        elif not self.options.list:
            parser.error("[-] Please provide a wordlist to use.")
        elif not self.options.timeout:
            parser.error("[-] Please provide timeout in seconds.")
        elif not self.options.outputfile:
            parser.error("[-] Please provide an output file to use.")
        return self.options

    def __request_url(self, url, time=2):
        try:
            r = requests.get(url, timeout=time)
            return r
        except Exception:
            pass

    def Enumerate_list(self):
        data = self.get_args()
        wordlist = data.list 
        time = int(data.timeout)
        OutputFile = data.outputfile
        subdomains = []

        try:
            with open(wordlist, "r") as words:
                alive = 0
                for word in words:
                    word = word.strip()
                    link = 'http://' + word + '.' + data.url
                    response = self.__request_url(link, time)
                    if response:
                        print(f"{green}[+] {link}")
                        subdomains.append(link)
                        alive += 1
            print(f"{yellow}\n[+] TOTAL FOUND SUBDOMAINS : {alive}")

            for i in subdomains:
                with open(OutputFile, "a") as subd:
                    subd.write(i+'\n')

        except FileNotFoundError as FNFE:
            print(f"[!] {red} Wordlist file does not exist !!")
        
        except KeyboardInterrupt:
            print(f"\n{red}[-] Exiting, bye :)")

if __name__=='__main__':
    target = SubLister()
    target.Enumerate_list()
    
    # Add arguments for url to parse, wordlist to use, save to file, response time etc.