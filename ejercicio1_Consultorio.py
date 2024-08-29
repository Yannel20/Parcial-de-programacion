class Paciente:
    def __init__(self, nombre, motivo_consulta):
        self.nombre = nombre
        self.motivo_consulta = motivo_consulta
        self.fecha_consulta = None

class ConsultorioMedico:
    def __init__(self):
        self.pacientes_registrados = {}  # Almacena los pacientes registrados por nombre
        self.sala_espera = []  # Lista de pacientes en la sala de espera

    def registrar_paciente(self, nombre, motivo_consulta):
        if nombre in self.pacientes_registrados:
            print(f"El paciente {nombre} ya tiene una consulta previa. Pasando a sala de espera.")
            self.sala_espera.append(nombre)
        else:
            nuevo_paciente = Paciente(nombre, motivo_consulta)
            nuevo_paciente.fecha_consulta = self.asignar_fecha_consulta()
            self.pacientes_registrados[nombre] = nuevo_paciente
            print(f"Paciente {nombre} registrado con éxito. Fecha de consulta asignada: {nuevo_paciente.fecha_consulta}")

    def asignar_fecha_consulta(self):
        # Aquí se implementaría la lógica para asignar una fecha de consulta
        return "2024-09-01"

    def mostrar_sala_espera(self):
        if self.sala_espera:
            print("Pacientes en la sala de espera:")
            for paciente in self.sala_espera:
                print(f"- {paciente}")
        else:
            print("No hay pacientes en la sala de espera.")

    def mostrar_pacientes_registrados(self):
        if self.pacientes_registrados:
            print("Pacientes registrados:")
            for nombre, paciente in self.pacientes_registrados.items():
                print(f"- {nombre}: {paciente.motivo_consulta}, Fecha de consulta: {paciente.fecha_consulta}")
        else:
            print("No hay pacientes registrados.")


# Uso:
consultorio = ConsultorioMedico()
consultorio.registrar_paciente("Ana", "Dolor de cabeza")
consultorio.registrar_paciente("Luis", "Chequeo general")
consultorio.registrar_paciente("Ana", "Dolor de estómago")  # Paciente ya registrado

consultorio.mostrar_pacientes_registrados()
consultorio.mostrar_sala_espera()
