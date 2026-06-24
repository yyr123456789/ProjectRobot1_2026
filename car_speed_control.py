from car_direction_control import *

class PathExecutor:
    def __init__(self, base_speed: int = DEFAULT_MOTOR_SPEED):
        self.base_speed = base_speed
        self.task_list = []

    def add_task(self, action: str, duration_ms: int, custom_speed = None):
        run_spd = custom_speed if custom_speed is not None else self.base_speed
        self.task_list.append({
            "action": action,
            "time": duration_ms,
            "speed": run_spd
        })

    def execute_all(self):
        action_map = {
            "forward": move_forward,
            "backward": move_backward,
            "left": pivot_left,
            "right": pivot_right,
            "curve_l": curve_left,
            "curve_r": curve_right,
            "stop": full_stop
        }
        for task in self.task_list:
            func = action_map[task["action"]]
            func(task["speed"])
            sleep(task["time"])
        full_stop()
        display.show(Image.HAPPY)

if __name__ == "__main__":
    square = PathExecutor(700)
    square.add_task("forward", 2000)
    square.add_task("right", 1200)
    square.add_task("forward", 2000)
    square.add_task("right", 1200)
    square.add_task("forward", 2000)
    square.add_task("right", 1200)
    square.add_task("forward", 2000)
    square.add_task("stop", 500)
    square.execute_all()
