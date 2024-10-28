// #define CATCH_CONFIG_MAIN
#include <catch2/catch_test_macros.hpp>

// Function(s) to be tested
int add(int a, int b) {
    return a + b;
}

int subtract(int a, int b) {
    return a - b;
}

// Test cases
TEST_CASE("Addition tests", "[add]") {
    REQUIRE(add(2, 2) == 4);
    REQUIRE(add(-1, 1) == 0);
}

TEST_CASE("Subtraction tests", "[subtract]") {
    SECTION("Positive numbers") {
        REQUIRE(subtract(10, 5) == 5);
    }

    SECTION("Negative numbers") {
        REQUIRE(subtract(-5, -5) == 0);
    }
    
    SECTION("Mixed positive and negative numbers") {
        REQUIRE(subtract(5, -5) == 10);
    }
}
