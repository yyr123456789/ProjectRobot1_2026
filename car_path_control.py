from car_direction_control import *

class PathExecutor:
    def __init__(self, base_speed: int = DEFAULT_MOTOR_SPEED):
        self.base_running_speed = base_speed
        self.task_queue = []

    def add_movement_task(self, action_name: str, duration_ms: int, custom_speed = None):
        task_speed = custom_speed if custom_speed is not None else self.base_running_speed
        self.task_queue.append({
            "action": action_name,
            "time": duration_ms,
            "speed": task_speed
        })

    def run_all_stored_tasks(self):
        for single_task in self.task_queue:
            current_action = single_task["action"]
            run_time = single_task["time"]
            task_speed = single_task["speed"]

            if current_action == "forward":
                move_forward(task_speed)
            elif current_action == "backward":
                move_backward(task_speed)
            elif current_action == "left":
                pivot_turn_left(task_speed)
            elif current_action == "right":
                pivot_turn_right(task_speed)
            elif current_action == "curve_l":
                gentle_curve_left(task_speed)
            elif current_action == "curve_r":
                gentle_curve_right(task_speed)
            elif current_action == "stop":
                full_stop_car()

            sleep(run_time)
        full_stop_car()
        display.show(Image.HAPPY)

if __name__ == "__main__":
    square_path = PathExecutor(base_speed=700)
    square_path.add_movement_task("forward", 2000)
    square_path.add_movement_task("right", 1200)
    square_path.add_movement_task("forward", 2000)
    square_path.add_movement_task("right", 1200)
    square_path.add_movement_task("forward", 2000)
    square_path.add_movement_task("right", 1200)
    square_path.add_movement_task("forward", 2000)
    square_path.add_movement_task("stop", 500)
    square_path.run_all_stored_tasks()