from car_path_control import PathExecutor
from privacy_data_handler import save_face_data_locally, wipe_all_face_data

if __name__ == "__main__":
    save_face_data_locally("robot_primary_owner_001")

    demo_path = PathExecutor(base_speed=650)
    demo_path.add_movement_task("forward", 1500)
    demo_path.add_movement_task("left", 1000)
    demo_path.add_movement_task("forward", 1500)
    demo_path.add_movement_task("right", 1000)
    demo_path.add_movement_task("stop", 800)

    demo_path.run_all_stored_tasks()
    wipe_all_face_data()