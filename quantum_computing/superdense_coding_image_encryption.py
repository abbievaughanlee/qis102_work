# use superdense coding to encode and decode an image as an unserialized bitsream
from pathlib import Path

import cv2
import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator


# encodes two bits of information into one qubit 
def encode(a, b):  # a and b are two bits of information
    qc = QuantumCircuit(
        2, 2
    )  # creates a quantum circuit with two classical bits and two qubits
    # prepare the qubits by entangling them (H and CNOT)
    qc.h(0)
    qc.cx(0, 1)
    qc.save_statevector("sv1")
    # encode the first qubit based on the values of a and b
    if a == 0 and b == 0:
        qc.id(0)
    if b == 1:
        qc.z(0)
    if a == 1:
        qc.x(0)
    qc.save_statevector("sv2")
    
    backend = AerSimulator()
    qc_transpiled = transpile(qc, backend)
    result = backend.run(qc_transpiled).result()

    sv2 = result.data(0)["sv2"]
    encoded_qubit = np.array(sv2)
    return encoded_qubit

# decodes a qubit back into two bits of information as a string
def decode(qubit):
    # define the controlled not and hadamard gates with linear algebra:
    g_I = np.array([[1, 0], [0, 1]], dtype=complex)  # identity
    g_H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)  # hadamard gate
    H_zero = np.kron(g_H, g_I) # applies the hadamard gate onto the first qubit only
    c_not = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]) # CNOT gate

    # decode the first qubit into two bits of information by reversing the entanglement between it and the second qubit
    sv1 = np.dot(c_not, qubit) # apply the c-not gate 
    sv2 = np.dot(H_zero, sv1) # apply a hadamard gate to qubit 0
    sv3 = np.round(sv2.real).astype(int) # save the state vector's real entries
    # decoder:
    if sv3[0] == 1:
        return "00"
    elif sv3[1] == 1:
        return "10"
    elif sv3[2] == 1:
        return "01"
    elif sv3[3] == 1:
        return "11"
    else:
        return "00" 
    

def encode_img(pic):
    # read the image file
    file_name = pic
    file_path = Path(__file__).parent / file_name
    img = cv2.imread(file_path, 2)
    # define original image dimensions in order to reshape after decoding
    height, width = img.shape

    if img is None:
        raise FileNotFoundError(f"Image file '{file_path}' not found.")

    # convert to Grayscale form, set a threshold mark (pixels above the mark will turn white and below the mark will turn black)
    ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    # convert to binary form
    #bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    binary_string = "".join(format(pixel, "08b") for row in bw_img for pixel in row)

    # encode every two bits of the binary string into a qubit
    qubits = []
    for i in range(0, len(binary_string) - 2, 2):
        qubits.append(encode(int(binary_string[i]), int(binary_string[i + 1])))
    return qubits, height, width

# decodes a series of qubits back into bits of information and returns a string of binary information
def decode_img(qubit_array):
    bin_str = ""
    for i in qubit_array:
        to_add = str(decode(i))
        bin_str += to_add
    return bin_str

def main():
    # encode catcig image, save each of the returned values as separate variables
    qubits = encode_img("cigcat.jpg")[0]
    height = encode_img("cigcat.jpg")[1]
    width = encode_img("cigcat.jpg")[2]

    # decode the encoded image back into a binary string
    bin_str = decode_img(qubits)

    # convert the binary string into numerical format:

    # converts each 8-bit chunk of the binary string back into an integer value representing the pixel intensity
    pixel_values = [int(bin_str[i:i+8], 2) for i in range(0, len(bin_str), 8)]  
    # reshapes the flat list of pixel values into the original 2D shape of the image.
    image_array = np.array(pixel_values, dtype=np.uint8)

    # Reshape the array to the original dimensions
    image = image_array.reshape((height, width))

    # Show the image using OpenCV
    cv2.imshow("Binary", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()
