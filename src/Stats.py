from datetime import datetime


class Stats:
    def __init__(self) -> None:
        self.accountData = {}

    def initNewAccount(self, accountName: str):
        self.accountData[accountName] = {
            "lastCheck": "",
            "totalDrops": 0,
            "sessionDrops": 0,
            "lastDrop": "[cyan]本次启动还没有掉落哦",
            "liveMatches": "",
            "status": "[yellow]等待",
            "failedLoginCounter": 0,
            "lastDropCheck": int(datetime.now().timestamp() * 1e3),
            "valid": True
        }

    def update(self, accountName: str, newDrops: int = 0, liveMatches: str = "", lastDropleague: str = None,
               reward: str = None):
        self.accountData[accountName]["lastCheck"] = datetime.now().strftime("%H:%M:%S %d/%m")
        self.accountData[accountName]["liveMatches"] = liveMatches
        if newDrops > 0:
            self.accountData[accountName]["sessionDrops"] += newDrops
            if reward and lastDropleague:
                self.accountData[accountName]["lastDrop"] = datetime.now().strftime(
                    "%H:%M:%S %d/%m") + f' ({lastDropleague})' + f' ({reward})'
            elif lastDropleague:
                self.accountData[accountName]["lastDrop"] = datetime.now().strftime(
                    "%H:%M:%S %d/%m") + f' ({lastDropleague})'
            else:
                self.accountData[accountName]["lastDrop"] = datetime.now().strftime("%H:%M:%S %d/%m")

    def updateThreadStatus(self, accountName: str):
        self.accountData[accountName]["valid"] = not self.accountData[accountName]["valid"]

    def getThreadStatus(self, accountName: str) -> bool:
        return self.accountData[accountName]["valid"]

    def setTotalDrops(self, accountName: str, amount: int):
        self.accountData[accountName]["totalDrops"] = amount

    def updateStatus(self, accountName: str, msg: str):
        self.accountData[accountName]["status"] = msg

    def updateLastDropCheck(self, accountName: str, lastDropCheck: int):
        self.accountData[accountName]["lastDropCheck"] = lastDropCheck

    def getLastDropCheck(self, accountName: str) -> int:
        return self.accountData[accountName]["lastDropCheck"]

    def addLoginFailed(self, accountName: str):
        self.accountData[accountName]["failedLoginCounter"] += 1

    def resetLoginFailed(self, accountName: str):
        self.accountData[accountName]["failedLoginCounter"] = 0

    def getFailedLogins(self, accountName: str):
        return self.accountData[accountName]["failedLoginCounter"]
