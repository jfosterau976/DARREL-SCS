import unittest

from core.telemetry import Telemetry


class TelemetryContractTests(unittest.TestCase):

    def test_export_contains_stable_top_level_contract(self):
        telemetry = Telemetry()
        telemetry.start("Telemetry contract test")
        telemetry.finish()

        exported = telemetry.export()

        self.assertEqual(
            set(exported),
            {
                "pulse_id",
                "question",
                "start_time",
                "end_time",
                "total_time_ms",
                "modules",
                "module_times",
                "memory_count",
                "llm",
                "verification_confidence",
                "executive_confidence",
                "neural_routing",
                "cognitive_budget",
                "status",
                "errors",
            },
        )

    def test_export_is_a_defensive_snapshot(self):
        telemetry = Telemetry()
        telemetry.start("Telemetry isolation test")
        telemetry.modules.append("attention_router")
        telemetry.module_times["attention_router"] = 1.25
        telemetry.errors.append({"type": "example"})
        telemetry.neural_routing = {
            "mode": "shadow",
            "authority": False,
            "comparison": {"exact_module_match": True},
        }
        telemetry.cognitive_budget = {
            "mode": "shadow",
            "authority": False,
            "enforced": False,
            "comparison": {"within_budget": True},
        }

        exported = telemetry.export()
        exported["modules"].append("injected")
        exported["module_times"]["attention_router"] = 999
        exported["errors"][0]["type"] = "mutated"
        exported["neural_routing"]["authority"] = True
        exported["neural_routing"]["comparison"][
            "exact_module_match"
        ] = False
        exported["cognitive_budget"]["enforced"] = True

        fresh = telemetry.export()

        self.assertEqual(fresh["modules"], ["attention_router"])
        self.assertEqual(fresh["module_times"]["attention_router"], 1.25)
        self.assertEqual(fresh["errors"][0]["type"], "example")
        self.assertFalse(fresh["neural_routing"]["authority"])
        self.assertTrue(
            fresh["neural_routing"]["comparison"]["exact_module_match"]
        )
        self.assertFalse(fresh["cognitive_budget"]["enforced"])


if __name__ == "__main__":
    unittest.main()
