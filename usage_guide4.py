"""
🤖 Gemini Agent System - Usage Guide

This system demonstrates 3 execution levels × 3 execution methods = 9 different ways to run agents.

EXECUTION LEVELS:
1. Agent Level - Agent-specific context and behavior
2. Run Level - Single execution context with parameters  
3. Global Level - System-wide context and state

EXECUTION METHODS:
1. run - Asynchronous execution
2. run_sync - Synchronous execution
3. streaming - Real-time streaming response

USAGE EXAMPLES:
"""

import asyncio
from main import GeminiAgent, AgentConfig, ExecutionMethod, ExecutionLevel

async def usage_examples():
    """Demonstrate different usage patterns"""
    
    # Create agent
    config = AgentConfig(name="ExampleAgent")
    agent = GeminiAgent(config)
    
    print("🎯 USAGE EXAMPLES")
    print("="*50)
    
    # Example 1: Agent Level + Run
    print("\n1️⃣ Agent Level + Async Run:")
    result = await agent.execute_query(
        "What is machine learning?",
        ExecutionMethod.RUN,
        ExecutionLevel.AGENT_LEVEL,
        {"context": "educational"}
    )
    
    # Example 2: Run Level + Sync
    print("\n2️⃣ Run Level + Sync Run:")
    result = await agent.execute_query(
        "Explain Python basics",
        ExecutionMethod.RUN_SYNC,
        ExecutionLevel.RUN_LEVEL,
        {"difficulty": "beginner"}
    )
    
    # Example 3: Global Level + Streaming
    print("\n3️⃣ Global Level + Streaming:")
    agent.update_global_context("user_level", "advanced")
    agent.update_global_context("preferred_style", "detailed")
    
    async for chunk in agent.execute_query(
        "How does neural network work?",
        ExecutionMethod.STREAMING,
        ExecutionLevel.GLOBAL_LEVEL,
        {"topic": "deep_learning"}
    ):
        pass  # Streaming output is handled in the method
    
    print("\n✅ Usage examples completed!")

# Quick test function
async def quick_test():
    """Quick test of all combinations"""
    config = AgentConfig(name="QuickTestAgent")
    agent = GeminiAgent(config)
    
    query = "What is AI?"
    
    print("🚀 QUICK TEST - All Combinations")
    print("="*40)
    
    combinations = [
        (ExecutionLevel.AGENT_LEVEL, ExecutionMethod.RUN),
        (ExecutionLevel.AGENT_LEVEL, ExecutionMethod.RUN_SYNC),
        (ExecutionLevel.AGENT_LEVEL, ExecutionMethod.STREAMING),
        (ExecutionLevel.RUN_LEVEL, ExecutionMethod.RUN),
        (ExecutionLevel.RUN_LEVEL, ExecutionMethod.RUN_SYNC),
        (ExecutionLevel.RUN_LEVEL, ExecutionMethod.STREAMING),
        (ExecutionLevel.GLOBAL_LEVEL, ExecutionMethod.RUN),
        (ExecutionLevel.GLOBAL_LEVEL, ExecutionMethod.RUN_SYNC),
        (ExecutionLevel.GLOBAL_LEVEL, ExecutionMethod.STREAMING),
    ]
    
    for i, (level, method) in enumerate(combinations, 1):
        print(f"\n🔄 Test {i}/9: {level.value} + {method.value}")
        
        try:
            if method == ExecutionMethod.STREAMING:
                async for chunk in agent.execute_query(query, method, level):
                    pass
            else:
                result = await agent.execute_query(query, method, level)
            
            print("✅ Success")
        except Exception as e:
            print(f"❌ Error: {e}")
        
        await asyncio.sleep(0.5)  # Small delay
    
    print(f"\n🎉 Quick test completed!")

if __name__ == "__main__":
    print("Choose test mode:")
    print("1. Usage Examples")
    print("2. Quick Test")
    
    choice = input("Enter choice (1 or 2): ").strip()
    
    if choice == "1":
        asyncio.run(usage_examples())
    else:
        asyncio.run(quick_test())
