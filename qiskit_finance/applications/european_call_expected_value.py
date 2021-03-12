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

"""The European Call Option Expected Value."""
from typing import Tuple

from qiskit.circuit.library import LinearAmplitudeFunction
from qiskit.algorithms.amplitude_estimators import EstimationProblem
from .estimation_application import EstimationApplication
from ..circuit.library.payoff_functions.european_call_expected_value import EuropeanCallExpectedValue as ECEV_Circ


class EuropeanCallExpectedValue(EstimationApplication):
    """The European Call Option Expected Value.
    Evaluates the expected payoff for a European call option given an uncertainty model.
    The payoff function is f(S, K) = max(0, S - K) for a spot price S and strike price K.
    """

    def __init__(self,
                 num_state_qubits: int,
                 strike_price: float,
                 rescaling_factor: float,
                 bounds: Tuple[float, float],
                 ) -> None:
        """
        Args:
            num_state_qubits: The number of qubits used to represent the random variable.
            strike_price: strike price of the European option
            rescaling_factor: approximation factor for linear payoff
            bounds: The bounds of the discretized random variable.
        """

        self._ecev_circ = ECEV_Circ(num_state_qubits=num_state_qubits, strike_price=strike_price,
                                    rescaling_factor=rescaling_factor, bounds=bounds)

        self._num_state_qubits = num_state_qubits

        # # create piecewise linear amplitude function
        # breakpoints = [bounds[0], strike_price]
        # slopes = [0, 1]
        # offsets = [0, 0]
        # f_min = 0
        # f_max = bounds[1] - strike_price
        # european_call = LinearAmplitudeFunction(
        #     num_state_qubits,
        #     slopes,
        #     offsets,
        #     domain=bounds,
        #     image=(f_min, f_max),
        #     breakpoints=breakpoints,
        #     rescaling_factor=rescaling_factor)

        # super().__init__(*european_call.qregs, name='ECEV')
        # self._data = european_call.data
        # self._european_call = european_call

    def to_estimation_problem(self):
        ep = EstimationProblem(state_preparation=self._ecev_circ,
                               objective_qubits=[self._num_state_qubits])

    # def post_processing(self, scaled_value: float) -> float:
    #     """Map the scaled value back to the original domain.
    #     Args:
    #         scaled_value: The scaled value.
    #     Returns:
    #         The scaled value mapped back to the original domain.
    #     """
    #     return self._european_call.post_processing(scaled_value)
