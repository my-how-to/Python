# ==============================================
# Pattern Name: Singleton
# Pattern Type: Creational
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
# Description:
#   The Singleton pattern ensures a class has only one instance
#   and provides a global access point to it.
#   In this example, the Logger class writes all messages to a
#   single shared log file, no matter how many loggers are created.
#
# Classifier:
#   - Category: Creational
#   - Purpose: Ensure only one instance of a class exists.
#   - Key idea: Centralize access to a shared resource.
#   - Common use: Logging, configuration, database connections.
#
# What Makes It Unique:
#   Singleton controls access rather than construction.
#   It restricts creation to a single instance 
#   and provides a consistent global reference.
# ==============================================

# -----------------------------
# Singleton class (Logger)
# -----------------------------
class Logger:
    """A Singleton that writes messages to one shared log file."""

    _instance = None

    def __new__(cls):
        """Create or return the existing instance."""
        if cls._instance is None:
            print("Initializing the logger...")
            cls._instance = super().__new__(cls)
            cls._instance.log_file = []  # simple in-memory log
        return cls._instance

    def write(self, message):
        """Write a message to the shared log."""
        self.log_file.append(message)
        print(f"[LOG] {message}")

    def show_logs(self):
        """Display all logged messages."""
        print("\n All log entries:")
        for line in self.log_file:
            print(line)


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    print("--- Singleton Pattern Example ---")

    log1 = Logger()
    log1.write("log1. System started.")
    log1.write("log1. Running diagnostics...")

    log2 = Logger()
    log2.write("log2. Diagnostics completed.")
    log2.show_logs()

    print("\n log1 is log2:", log1 is log2)


# -----------------------------
# Example Output
# -----------------------------
# --- Singleton Pattern Example ---
# Initializing the logger...
# [LOG] System started.
# [LOG] Running diagnostics...
# [LOG] Diagnostics completed.
#
# All log entries:
# System started.
# Running diagnostics...
# Diagnostics completed.
#
# log1 is log2: True


# ==============================================
# History
# ==============================================
# The Singleton pattern was popularized by the Gang of Four in 1994.
# It provided a structured way to manage shared global resources like
# loggers, configuration files, and database connections — replacing
# error-prone global variables used in earlier systems.
# ==============================================