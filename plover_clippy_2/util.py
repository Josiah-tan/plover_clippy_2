from datetime import datetime


def noNewOutput(new):
    for a in reversed(new):
        if a.text and not a.text.isspace():
            return False
    return True
# for a in reversed(new):
#     if a.text and not a.text.isspace():
#         break
# else:
#     return


def getOrgDate():
    return datetime.now().strftime("%Y-%m-%d %a %H:%M")
