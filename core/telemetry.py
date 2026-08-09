from copy import deepcopy
from datetime import datetime
import time
import uuid


class Telemetry:

    def __init__(self):

        self.reset()

    def reset(self):

        self.pulse_id = str(uuid.uuid4())[:8]

        self.question = ""

        self.start_time = None

        self.end_time = None

        self.module_times = {}

        self.modules = []

        self.status = "RUNNING"

        self.errors = []

        self.memory_count = 0

        self.llm = ""

        self.verification_confidence = 0

        self.executive_confidence = 0

        self.neural_routing = {}

        self.cognitive_budget = {}

    def start(self, question):

        self.reset()

        self.question = question

        self.start_time = datetime.now()

        self._timer = time.perf_counter()

    def begin_module(self):

        return time.perf_counter()

    def end_module(self, name, timer):

        elapsed = round(
            (time.perf_counter() - timer) * 1000,
            2
        )

        self.module_times[name] = elapsed

        if name not in self.modules:

            self.modules.append(name)

    def finish(self):

        self.end_time = datetime.now()

        self.status = "COMPLETE"

    def total_time(self):

        if self.start_time is None or self.end_time is None:

            return 0

        return round(

            (self.end_time - self.start_time).total_seconds() * 1000,

            2

        )

    def export(self):

        return deepcopy({

            "pulse_id": self.pulse_id,

            "question": self.question,

            "start_time": str(self.start_time),

            "end_time": str(self.end_time),

            "total_time_ms": self.total_time(),

            "modules": self.modules,

            "module_times": self.module_times,

            "memory_count": self.memory_count,

            "llm": self.llm,

            "verification_confidence":
                self.verification_confidence,

            "executive_confidence":
                self.executive_confidence,

            "neural_routing": self.neural_routing,

            "cognitive_budget": self.cognitive_budget,

            "status": self.status,

            "errors": self.errors

        })


telemetry = Telemetry()
