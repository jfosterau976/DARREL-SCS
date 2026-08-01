from core.scs_executive import scs_executive
from core.pulse_orchestrator import pulse_orchestrator


def run_full_pulse(question):

    print("\nSCS FULL COGNITIVE PULSE")
    print("=" * 35)


    executive_result = scs_executive.process(
        question
    )


    print("\nEXECUTIVE RESULT:")
    print(executive_result)


    strategy = executive_result["decision"]["strategy"]


    pulse_result = pulse_orchestrator.run_pulse(
        strategy
    )


    print("\nPULSE RESULT:")
    print(pulse_result)



if __name__ == "__main__":

    run_full_pulse(
        "Should SCS use multiple agents?"
    )