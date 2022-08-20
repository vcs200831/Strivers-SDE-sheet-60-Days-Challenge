class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        maxH=[]
        tank=startFuel
        prevPos=0
        visited=0
        
        for curPos,fuelAval in stations+[[target,0]]:
          tank = tank-(curPos-prevPos)
          while tank<0 and maxH:
            tank=tank+(-heappop(maxH))
            visited=visited+1
          if tank<0: return -1
          
          heappush(maxH,-fuelAval)
          
            
          prevPos=curPos
          
        return visited
          
        