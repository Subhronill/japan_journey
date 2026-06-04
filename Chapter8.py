# Robot Class — Chapter 8
# Your first robotics-flavored Python code

class Robot:
    
    def __init__(self, name, robot_type):
        self.name = name
        self.robot_type = robot_type
        self.is_active = False
        self.battery = 100
        self.position = {"x": 0, "y": 0}
        self.actions_log = []
    
    def activate(self):
        if not self.is_active:
            self.is_active = True
            self.log_action("System activated")
            print(f"{self.name} online. All systems ready.")
        else:
            print(f"{self.name} is already active.")
    
    def move(self, direction, distance):
        if not self.is_active:
            print("Cannot move. Robot is offline.")
            return
        
        if self.battery < 10:
            print("Battery critical. Cannot move.")
            return
        
        if direction == "north":
            self.position["y"] += distance
        elif direction == "south":
            self.position["y"] -= distance
        elif direction == "east":
            self.position["x"] += distance
        elif direction == "west":
            self.position["x"] -= distance
        else:
            print(f"Unknown direction: {direction}")
            return
        
        self.battery -= distance * 2
        action = f"Moved {direction} {distance}m → position {self.position}"
        self.log_action(action)
        print(action)
    
    def log_action(self, action):
        self.actions_log.append(action)
    
    def status(self):
        state = "ACTIVE" if self.is_active else "OFFLINE"
        print(f"╔══════════════════════════════╗")
        print(f"║  ROBOT: {self.name:<21}║")
        print(f"║  Type:  {self.robot_type:<21}║")
        print(f"║  State: {state:<21}║")
        print(f"║  Battery: {self.battery}%{'':<18}║")
        print(f"║  Position: x={self.position['x']}, y={self.position['y']}{'':<12}║")
        print(f"║  Actions logged: {len(self.actions_log):<13}║")
        print(f"╚══════════════════════════════╝")

# Create and operate your first robot
airo = Robot("AIRO-01", "Autonomous Navigation")

airo.status()
airo.activate()
airo.move("north", 5)
airo.move("east", 3)
airo.move("north", 2)
airo.status()

print("\nAction Log:")
for i, action in enumerate(airo.actions_log, 1):
    print(f"  {i}. {action}")