class AAMEngine:
    """
    Public demonstration interface of AAM Predict.

    The proprietary analytical engine,
    mathematical models and calibration modules
    are not included in this repository.
    """

    def calculate(self, tsh: float, t4: float, atpo: float) -> dict:

        return {
            "mode": "Demo",
            "status": "Core algorithm unavailable",
            "message": (
                "This public repository contains a demonstration version only. "
                "The proprietary analytical engine is excluded."
            ),
            "inputs": {
                "TSH": tsh,
                "T4": t4,
                "ATPO": atpo
            }
        }
