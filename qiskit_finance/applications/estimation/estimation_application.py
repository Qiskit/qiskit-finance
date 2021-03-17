# This code is part of Qiskit.
#
# (C) Copyright IBM 2018, 2021.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""An abstract class for estimation application classes."""
from abc import ABC, abstractmethod

from qiskit.algorithms.amplitude_estimators import EstimationProblem


class EstimationApplication(ABC):
    """
    An abstract class for estimation applications
    """

    @abstractmethod
    def to_estimation_problem(self) -> EstimationProblem:
        """Convert a problem instance into a
        :class:`~qiskit.algorithms.amplitude_estimators.EstimationProblem`
        """
        pass
