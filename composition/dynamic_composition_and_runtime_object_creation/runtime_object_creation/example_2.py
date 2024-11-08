class IntelProcessor:
    def __init__(self):
        self.cores = 5
        self.clock_speed = 3.6
        self.model = "Intel i5"

    @staticmethod
    def process():
        print("Intel processor processing data....")

    def show_speces(self):
        print(f"{self.model}: {self.cores} cores at {self.clock_speed} GHz.")


class AMDProcessor:
    def __init__(self):
        self.cores = 8
        self.clock_speed = 3.9
        self.model = "AMD Ryzen 7"

    @staticmethod
    def process():
        print("AMD processor processing data....")

    def show_speces(self):
        print(f"{self.model}: {self.cores} cores at {self.clock_speed} GHz.")


class ARMProcessor:
    def __init__(self):
        self.cores = 6
        self.clock_speed = 2.5
        self.model = "ARM Cortex-A78"

    @staticmethod
    def process():
        print("ARM processor processing data....")

    def show_speces(self):
        print(f"{self.model}: {self.cores} cores at {self.clock_speed} GHz.")

processor_types = {
    'Intel': IntelProcessor,
    'AMD': AMDProcessor,
    'ARM': ARMProcessor
}

class Computer:
    def __init__(self, processor_type):
        if processor_type in processor_types:
            self.processor = processor_types[processor_type]()
            print(f"{processor_type} processor initialized.")
        else:
            raise ValueError("Unknown processor type.")

    def start(self):
        print("Computer starting with processor:")
        self.processor.process()
        self.processor.show_speces()

    def execute_task(self, task):
        print(f"Executing task: {task}...")
        self.processor.process()
        print("Task Completed.")

    @staticmethod
    def shutdown():
        print("Computer shutting down.")

computer_with_intel = Computer("Intel")
computer_with_intel.start()
computer_with_intel.execute_task("Data Analysis")
computer_with_intel.shutdown()



computer_with_amd = Computer("AMD")
computer_with_amd.start()
computer_with_amd.execute_task("Machine Learning Training")
computer_with_amd.shutdown()


computer_with_arm = Computer("ARM")
computer_with_arm.start()
computer_with_arm.execute_task("Mobile Application Processing")
computer_with_arm.shutdown()
