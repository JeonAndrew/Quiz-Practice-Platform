#include <iostream>

#include "crow.h" // Include Crow's single header

int main() {
    crow::SimpleApp app; // Initialize Crow application

    // Define a basic route for the root URL "/"
    CROW_ROUTE(app, "/")([]() {
        return "Hello, World!";
    });

    // Define a GET route for "/hello"
    CROW_ROUTE(app, "/hello")
    ([]() {
        return "Hello from the C++ server!";
    });

    // Define a POST route that accepts JSON data
    CROW_ROUTE(app, "/data").methods(crow::HTTPMethod::POST)
    ([](const crow::request& req) {
        auto json_data = crow::json::load(req.body);
        if (!json_data) {
            return crow::response(400, "Invalid JSON");
        }
        std::string name = json_data["name"].s();
        int age = json_data["age"].i();

        // Respond with a JSON message
        crow::json::wvalue response;
        response["message"] = "Data received";
        response["name"] = name;
        response["age"] = age;

        return crow::response(response);
    });

    // Define a wildcard route with parameter
    CROW_ROUTE(app, "/greet/<string>")
    ([](std::string name) {
        return "Hello, " + name + "!";
    });

    // Set the server to listen on port 8080
    app.port(8080).multithreaded().run();
}
