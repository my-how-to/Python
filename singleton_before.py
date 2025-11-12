# ==============================================
# Before Pattern: Singleton
# Pattern Type: Creational
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
# Description:
#   Demonstrates how developers handled shared resources before the Singleton pattern.
#   In this version, multiple Logger instances exist independently, each keeping its
#   own log. This leads to inconsistent and fragmented log data.
#
# Classifier:
#   - Category: Creational
#   - Purpose: Show how resource management looked before Singleton.
#   - Key idea: Each object keeps its own state — no shared resource.
#   - Common issue: Duplicated, inconsistent, or lost data across instances.
# ==============================================

# -----------------------------
# Regular Logger class (no Singleton)
# -----------------------------
class Logger:
    """Each logger instance keeps its own log data — no shared state."""

    def __init__(self, name):
        self.name = name
        self.log_file = []

    def write(self, message):
        """Write a message to this logger's local log file."""
        self.log_file.append(message)
        print(f"[{self.name}] {message}")

    def show_logs(self):
        """Display all log entries for this instance only."""
        print(f"\nLogs from {self.name}:")
        for line in self.log_file:
            print(f"{self.name}: {line}")


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    print("--- Before Singleton Example ---")

    # Each part of the program creates its own logger.
    log1 = Logger("Logger-1")
    log2 = Logger("Logger-2")

    log1.write("System started.")
    log2.write("Running diagnostics...")
    log1.write("Diagnostics completed.")

    # Each logger has its own independent log.
    log1.show_logs()
    log2.show_logs()


# -----------------------------
# Example Output
# -----------------------------
# --- Before Singleton Example ---
# [Logger-1] System started.
# [Logger-2] Running diagnostics...
# [Logger-1] Diagnostics completed.
#
# Logs from Logger-1:
# Logger-1: System started.
# Logger-1: Diagnostics completed.
#
# Logs from Logger-2:
# Logger-2: Running diagnostics...


# ==============================================
# History
# ==============================================
# Before the Singleton pattern, developers often created multiple independent
# instances for shared resources such as loggers or configuration managers.
# This caused fragmentation and inconsistency. The Singleton pattern centralized
# access, ensuring a single point of control for shared system components.
# ==============================================