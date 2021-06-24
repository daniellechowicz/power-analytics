from report.report import AutoReport, Report
import threading


class ReportThread(threading.Thread):
    """
    This class uses threading module to be able
    to generate report in background without freezing the application.
    """

    def __init__(
        self,
        x_init,
        y_init,
        idle_region,
        cutting_region,
        metadata,
        stats,
        path,
        auto_generated,
    ):
        super().__init__()
        self.x_init = x_init
        self.y_init = y_init
        self.idle_region = idle_region
        self.cutting_region = cutting_region
        self.metadata = metadata
        self.stats = stats
        self.path = path
        self.auto_generated = auto_generated

    def run(self):
        if self.auto_generated:
            AutoReport(
                self.x_init,
                self.y_init,
                self.idle_region,
                self.cutting_region,
                self.metadata,
                self.stats,
                self.path,
            )
        else:
            Report(
                self.x_init,
                self.y_init,
                self.idle_region,
                self.cutting_region,
                self.metadata,
                self.stats,
                self.path,
            )
