from car_path_control import PathExecutor
from privacy_data_handler import store_face_data, clear_all_data

if __name__ == "__main__":
    store_face_data("robot_main_owner_001")

    demo_route = PathExecutor(650)
    demo_route.add_task("forward", 1500)
    demo_route.add_task("left", 1000)
    demo_route.add_task("forward", 1500)
    demo_route.add_task("right", 1000)
    demo_route.add_task("stop", 800)

    demo_route.execute_all()
    clear_all_data()
