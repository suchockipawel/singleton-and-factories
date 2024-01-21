from worker import DeliveryMan, Packager


# Complete the method create_object
class WorkerFactory:
    @staticmethod
    def create_object(worker_type):
        if worker_type == "packager": # * If the parameter worker_type is equal to `"packager"`, create an instance of **Packager**
            return Packager()
        elif worker_type == "delivery": # * If the parameter worker_type is equal to `"delivery"`, create an instance of **DeliveryMan**
            return DeliveryMan()
        

