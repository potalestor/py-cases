from typing import List

class BrowserHistory:
 
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr = 0
        self.bound = 0

    def visit(self, url: str) -> None:
        self.curr += 1
        if self.curr == len(self.history):
            self.history.append(url)
        else:
            self.history[self.curr] = url
        self.bound = self.curr

    def back(self, steps: int) -> str:
        self.curr = max(self.curr - steps, 0)
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = min(self.curr + steps, self.bound)
        return self.history[self.curr]


'''
Input:
["BrowserHistory","visit","back","back","back","forward","forward","visit","visit","visit","visit","visit","visit","visit","visit","back","visit","forward","back","back","forward","visit","visit","visit","back","visit","forward","visit","visit","visit","visit","back","back","visit","forward","back","visit","visit","back","forward","forward"]
[["vvlf.com"],["rwrjffk.com"],[9],[6],[10],[6],[5],["af.com"],["jjuulz.com"],["vqthh.com"],["viw.com"],["mvvxuo.com"],["sezid.com"],["ncbnmr.com"],["qehugwp.com"],[7],["wg.com"],[9],[6],[4],[2],["foy.com"],["szi.com"],["yqxprn.com"],[9],["pmgoa.com"],[3],["dkik.com"],["mxlcs.com"],["mvs.com"],["uuto.com"],[4],[1],["mdhkz.com"],[9],[9],["zwcc.com"],["afsdng.com"],[6],[1],[3]]
Output:
[null,null,"vvlf.com","vvlf.com","vvlf.com","rwrjffk.com","rwrjffk.com",null,null,null,null,null,null,null,null,"af.com",null,"wg.com","vvlf.com","vvlf.com","rwrjffk.com",null,null,null,"vvlf.com",null,"pmgoa.com",null,null,null,null,"pmgoa.com","vvlf.com",null,"mdhkz.com","vvlf.com",null,null,"vvlf.com","zwcc.com","afsdng.com"]
Expected:
[null,null,"vvlf.com","vvlf.com","vvlf.com","rwrjffk.com","rwrjffk.com",null,null,null,null,null,null,null,null,"af.com",null,"wg.com","vvlf.com","vvlf.com","af.com",null,null,null,"vvlf.com",null,"pmgoa.com",null,null,null,null,"pmgoa.com","vvlf.com",null,"mdhkz.com","vvlf.com",null,null,"vvlf.com","zwcc.com","afsdng.com"]
'''

browserHistory = BrowserHistory("leetcode.com")
browserHistory.visit("google.com")       # You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com")     # You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com")      # You are in "facebook.com". Visit "youtube.com"
print(browserHistory.back(1))                   # You are in "youtube.com", move back to "facebook.com" return "facebook.com"
print(browserHistory.back(1))                   # You are in "facebook.com", move back to "google.com" return "google.com"
print(browserHistory.forward(1))                # You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com")     # You are in "facebook.com". Visit "linkedin.com"
print(browserHistory.forward(2))                # You are in "linkedin.com", you cannot move forward any steps.
print(browserHistory.back(2))                   # You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
print(browserHistory.back(7))                   # You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"