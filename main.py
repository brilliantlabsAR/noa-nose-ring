from llms.core.noa_rose_ring import AI_Nose_Ring

def main():
    # Instantiate AI Nose Ring
    nose_ring = AI_Nose_Ring()

    # Connect to the AI Nose Ring
    nose_ring.connect()

    # Analyze the environment
    nose_ring.analyze_environment()

    # Get scent recommendations
    nose_ring.get_recommendations()

    # Adjust sensitivity
    nose_ring.adjust_sensitivity(7)

    # Disconnect from the AI Nose Ring
    nose_ring.disconnect()

if __name__ == "__main__":
    main()
