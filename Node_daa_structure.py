# Node and Route information data structure

class markerNode:
    """
    Save marker data
    Floor : current floor
    Id : id of the marker
    northConnectedNode : connected node which located in north
    southConnectedNode : connected node which located in south
    westConnectedNode : connected node which located in west
    eastConnectedNode : connected node which located in east
    nextNode : next node for the route

    1. Destination Node
        For elevator, toilet, exit etc
        Use Id from 1~50
    2. Marker Node
        For the way point
        Use Id from over 50
    """
    def __init__(self, floor, id, north = None, south = None, west = None, east = None):
        self.floor = floor
        self.id = id
        self.northConnectedNode = north
        self.southConnectedNode = south
        self.westConnectedNode = west
        self.eastConnectedNode = east
        self.next = None

class markerGraph:
    """
    Fixed map graph for Seolleung station
    Not made yet
    """
    def __init__(self):
        self.size = 1000

class routeData:
    """
    Stack the ordered route information
    """
    def __init__(self, markerNode = None):
        self.head = markerNode
        self.routeLength = 1

    def insertFirstNode(self, firstNode):
        new_node = firstNode
        temp_node = self.head
        self.head = new_node
        self.head.next = temp_node
        self.routeLength += 1

    def insertLast(self, insertNode):
        node = self.head
        while True:
            if node.next == None:
                break
            node = node.next

        new_node = insertNode
        node.next = new_node
        self.routeLength += 1

    def deleteHead(self):
        node = self.head
        self.head = node.next
        del node

    def size(self):
        return str(self.routeLength)

def createB2mapInSeooleung():
    """
    Seolleung station marker nodes in B2 Floor
    :return: way points in Seolleung station B2
    """
    #railWay marker
    global railWay_7_4_Seolleung_B2
    global railWay_8_1_Seolleung_B2, railWay_8_2_Seolleung_B2, railWay_8_3_Seolleung_B2, railWay_8_4_Seolleung_B2
    global railWay_9_1_Seolleung_B2
    railWay_7_4_Seolleung_B2 = markerNode(2, 1, north = blockWay_51_Seolleung_B2, east = railWay_8_1_Seolleung_B2)
    railWay_8_1_Seolleung_B2 = markerNode(2, 2, west = railWay_7_4_Seolleung_B2, east = railWay_8_2_Seolleung_B2)
    railWay_8_2_Seolleung_B2 = markerNode(2, 2, west = railWay_8_1_Seolleung_B2, east = railWay_8_3_Seolleung_B2)
    railWay_8_3_Seolleung_B2 = markerNode(2, 2, west = railWay_8_2_Seolleung_B2, east = railWay_8_4_Seolleung_B2)
    railWay_8_4_Seolleung_B2 = markerNode(2, 2, west = railWay_8_3_Seolleung_B2, east = railWay_9_1_Seolleung_B2)
    railWay_9_1_Seolleung_B2 = markerNode(2, 2, west = railWay_8_4_Seolleung_B2)

    #blockWay marker
    global blockWay_51_Seolleung_B2, blockWay_52_Seolleung_B2
    blockWay_51_Seolleung_B2 = markerNode(2, 51, north = blockWay_52_Seolleung_B2, west = railWay_7_4_Seolleung_B2)
    blockWay_52_Seolleung_B2 = markerNode(2, 52, south = blockWay_51_Seolleung_B2, east = elevator_2_Seolleung_B2)

    #elevator marker
    global elevator_2_Seolleung_B2
    elevator_2_Seolleung_B2 = markerNode(2, 3, west = blockWay_52_Seolleung_B2)


def createB3mapInSeooleung():
    """
    Seolleung station marker nodes in B3 Floor
    :return: way points in Seolleung station B3
    """
    # railWay marker
    global railWay_2_4_Seolleung_B3
    railWay_2_4_Seolleung_B3 = markerNode(2, 1, north=blockWay_55_Seolleung_B3)

    # blockWay marker
    global blockWay_53_Seolleung_B3, blockWay_54_Seolleung_B3, blockWay_55_Seolleung_B3
    blockWay_53_Seolleung_B3 = markerNode(3, 53, south=blockWay_54_Seolleung_B3, east=elevator_2_Seolleung_B3)
    blockWay_54_Seolleung_B3 = markerNode(3, 54, north=blockWay_53_Seolleung_B3, east=blockWay_55_Seolleung_B3)
    blockWay_55_Seolleung_B3 = markerNode(3, 55, south=railWay_2_4_Seolleung_B3, east=blockWay_54_Seolleung_B3)

    #elevator marker
    global elevator_2_Seolleung_B3
    elevator_2_Seolleung_B3 = markerNode(3, 3, west = blockWay_53_Seolleung_B3)


def createB1mapInHanti():
    """
    Hanti station marker nodes in B4 Floor
    :return: way points in Hanti station B4
    """
    #railWay marker

    #blockWay marker
    global blockWay_59_Hanti_B1
    blockWay_59_Hanti_B1 = markerNode(1, 59, south = elevator_2_Hanti_B1, east = elevator_1_Hanti_B1)

    # elevator marker
    global elevator_1_Hanti_B1, elevator_2_Hanti_B1
    elevator_1_Hanti_B1 = markerNode(1, 7, west = blockWay_59_Hanti_B1)
    elevator_2_Hanti_B1 = markerNode(1, 8, north = blockWay_59_Hanti_B1)


def createB4mapInHanti():
    """
    Hanti station marker nodes in B4 Floor
    :return: way points in Hanti station B4
    """
    #railWay marker
    global railWay_2_4_Hanti_B4
    global railWay_3_1_Hanti_B4, railWay_3_2_Hanti_B4
    railWay_2_4_Hanti_B4 = markerNode(4, 4, west = railWay_3_1_Hanti_B4)
    railWay_3_1_Hanti_B4 = markerNode(4, 5, east = railWay_2_4_Hanti_B4, west = railWay_3_2_Hanti_B4)
    railWay_3_2_Hanti_B4 = markerNode(4, 6, north = blockWay_56_Hanti_B4, east = railWay_2_4_Hanti_B4)

    #blockWay marker
    global blockWay_56_Hanti_B4, blockWay_57_Hanti_B4, blockWay_58_Hanti_B4
    blockWay_56_Hanti_B4 = markerNode(4, 53, south = railWay_3_2_Hanti_B4,west = blockWay_57_Hanti_B4)
    blockWay_57_Hanti_B4 = markerNode(4, 54, north = blockWay_58_Hanti_B4, east = blockWay_56_Hanti_B4)
    blockWay_58_Hanti_B4 = markerNode(4, 55, south = blockWay_57_Hanti_B4, east= elevator_1_Hanti_B4)

    # elevator marker
    global elevator_1_Hanti_B4
    elevator_1_Hanti_B4 = markerNode(3, 3, east = blockWay_58_Hanti_B4)


def createRouteForTransfer():
    # Seolleung station B2 way point
    global routeDataList
    routeDataList = routeData(railWay_9_1_Seolleung_B2)
    routeDataList.insertLast(railWay_8_4_Seolleung_B2)
    routeDataList.insertLast(railWay_8_3_Seolleung_B2)
    routeDataList.insertLast(railWay_8_2_Seolleung_B2)
    routeDataList.insertLast(railWay_8_1_Seolleung_B2)
    routeDataList.insertLast(railWay_7_4_Seolleung_B2)
    routeDataList.insertLast(blockWay_51_Seolleung_B2)
    routeDataList.insertLast(blockWay_52_Seolleung_B2)
    routeDataList.insertLast(elevator_2_Seolleung_B2)
    routeDataList.insertLast(elevator_2_Seolleung_B3)
    routeDataList.insertLast(blockWay_53_Seolleung_B3)
    routeDataList.insertLast(blockWay_54_Seolleung_B3)
    routeDataList.insertLast(blockWay_55_Seolleung_B3)
    routeDataList.insertLast(railWay_2_4_Seolleung_B3)
    routeDataList.insertLast(railWay_2_4_Hanti_B4)
    routeDataList.insertLast(railWay_3_1_Hanti_B4)
    routeDataList.insertLast(railWay_3_2_Hanti_B4)
    routeDataList.insertLast(blockWay_56_Hanti_B4)
    routeDataList.insertLast(blockWay_57_Hanti_B4)
    routeDataList.insertLast(blockWay_58_Hanti_B4)
    routeDataList.insertLast(elevator_1_Hanti_B4)
    routeDataList.insertLast(elevator_1_Hanti_B1)
    routeDataList.insertLast(blockWay_59_Hanti_B1)
    routeDataList.insertLast(elevator_2_Hanti_B1)

class currentLocation:
    def __init__(self, floor, prev, cur, next):
        self.floor = floor
        self.prev = prev
        self.cur = cur
        self.next = next

    def updateFloor(self, floor):
        self.floor = floor

    def updateLocation(self, next):
        self.prev = self.cur
        self.cur = self.next
        self.next = next



#main function
if __name__ == '__main__':
    createB2mapInSeooleung()
    createRouteForTransfer()

    while True:
        pass