from core.agent_registry import agent_registry
from core.skill_manager import skill_manager


def boot():
    print("=" * 40)
    print(" Synthetic Cognitive System V0.1")
    print("=" * 40)

    print("\n[CORE SYSTEMS]")
    print("✓ Cognitive Controller: ONLINE")
    print("✓ Skill Manager: ONLINE")

    print("\n[AGENTS LOADED]")

    agents = agent_registry.list_all()

    for name, data in agents.items():
        print(f"✓ {name} - {data['role']}")

    print("\n[SKILLS AVAILABLE]")

    skills = skill_manager.list_skills()

    for skill in skills:
        print(f"✓ {skill}")

    print("\nSYSTEM STATUS: READY")


if __name__ == "__main__":
    boot()