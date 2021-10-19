import math
import numpy as np
import matplotlib.pyplot as plt
import copy

fixedPoint = [0,0]
closedList = [list([list([False for i in range(360)]) for j in range(360)]) for k in range(360)]

def getAngle(Angle):
    return closedList[Angle[0]][Angle[1]][Angle[2]]

def getAngle(Angle):
    closedList[Angle[0]][Angle[1]][Angle[2]] = True

def euclidian_dist(p1,p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

def heuristic_fn(goalPoint,endPoint,totalLength):
    return euclidian_dist(goalPoint,endPoint)/totalLength

def cylindrical_Coordinates(coordinate,length,angle):
    res_Cor = [0 ,0]
    res_Cor[0] = coordinate[0] + length*math.cos(math.radians(angle))
    res_Cor[1] = coordinate[1] + length*math.sin(math.radians(angle))
    return res_Cor

def arm_endPoint(initial_Cor,lengths,angles):
    endPoint = initial_Cor
    angle = 0
    for i in range(len(lengths)):
        angle += angles[i]
        endPoint = cylindrical_Coordinates(endPoint,lengths[i],angle)
    endPoint = np.round_(endPoint,decimals=3)
    return endPoint

def bfs(arms,initial_angles,goalPoint,increment,error):
    openlist = []
    closedlist = []
    openlist.append(initial_angles)
    step = 0
    while len(openlist)!=0:
        step += 1
        currAngle = openlist.pop(0)
        currAngle = list([num%360 for num in currAngle])
        closedlist.append(list(currAngle))
        if euclidian_dist(arm_endPoint(fixedPoint,arms,currAngle),goalPoint) < error:
            return currAngle
        for i in range(len(currAngle)):
            currAngle[i] += increment
            currAngle = list([num%360 for num in currAngle])
            if closedlist.count(currAngle)==0:
                openlist.append(list(currAngle))
            currAngle[i] -= 2*increment
            currAngle = list([num%360 for num in currAngle])
            if closedlist.count(currAngle)==0:
                openlist.append(list(currAngle))
            currAngle[i] += increment
            currAngle = list([num%360 for num in currAngle])
        # if step%10 == 0:
        #     print(closedlist)
        # print(euclidian_dist(arm_endPoint(fixedPoint,arms,currAngle),goalPoint))

def main():
    arms = [1,1,1]
    initial_angles = [60,300,300]
    goalPoint = [1,2]
    endPoint = arm_endPoint(fixedPoint,arms,initial_angles)
    print(endPoint)

    searchGoal = bfs(arms,initial_angles,goalPoint,10,0.3)
    print(searchGoal)
    print(arm_endPoint(fixedPoint,arms,searchGoal))


if __name__ == "__main__":
    main()