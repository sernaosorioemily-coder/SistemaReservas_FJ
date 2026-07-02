from modelos.cliente import Cliente
from modelos.reserva import Reserva

from servicios.reserva_sala import ReservaSala
from servicios.alquiler_equipo import AlquilerEquipo
from servicios.asesoria import Asesoria

from utilidades.logger import logger


def ejecutar_simulacion():

    print("=" * 60)
    print(" SISTEMA INTEGRAL DE GESTIÓN - SOFTWARE FJ")
    print("=" * 60)

    # -------------------------------------------------
    # OPERACIÓN 1 - Cliente válido
    # -------------------------------------------------
    try:
        cliente1 = Cliente("Juan Pérez", "juan@gmail.com")
        logger.info("Cliente registrado correctamente.")
        print("✔ Cliente 1 registrado.")
    except Exception as e:
        logger.error(e)

    # -------------------------------------------------
    # OPERACIÓN 2 - Cliente válido
    # -------------------------------------------------
    try:
        cliente2 = Cliente("María López", "maria@gmail.com")
        logger.info("Cliente registrado correctamente.")
        print("✔ Cliente 2 registrado.")
    except Exception as e:
        logger.error(e)

    # -------------------------------------------------
    # OPERACIÓN 3 - Cliente inválido
    # -------------------------------------------------
    try:
        Cliente("", "correo@gmail.com")
    except Exception as e:
        logger.error(e)
        print("❌ Error al registrar cliente.")

    # -------------------------------------------------
    # OPERACIÓN 4 - Correo inválido
    # -------------------------------------------------
    try:
        Cliente("Pedro", "correo")
    except Exception as e:
        logger.error(e)
        print("❌ Correo inválido.")

    # -------------------------------------------------
    # OPERACIÓN 5 - Servicio Sala
    # -------------------------------------------------
    try:
        sala = ReservaSala("Sala Premium", 50000)
        logger.info("Servicio Sala creado.")
        print("✔ Servicio Sala creado.")
    except Exception as e:
        logger.error(e)

    # -------------------------------------------------
    # OPERACIÓN 6 - Servicio Equipo
    # -------------------------------------------------
    try:
        equipo = AlquilerEquipo("VideoBeam", 30000)
        logger.info("Servicio Equipo creado.")
        print("✔ Servicio Equipo creado.")
    except Exception as e:
        logger.error(e)

    # -------------------------------------------------
    # OPERACIÓN 7 - Servicio Asesoría
    # -------------------------------------------------
    try:
        asesoria = Asesoria("Consultoría", 100000)
        logger.info("Servicio Asesoría creada.")
        print("✔ Servicio Asesoría creada.")
    except Exception as e:
        logger.error(e)

    # -------------------------------------------------
    # OPERACIÓN 8 - Reserva correcta
    # -------------------------------------------------
    try:
        reserva1 = Reserva(cliente1, sala, 3)
        reserva1.confirmar()

        costo = reserva1.procesar()

        print(f"✔ Reserva confirmada. Valor: ${costo}")

        logger.info("Reserva 1 realizada correctamente.")

    except Exception as e:
        logger.error(e)

    # -------------------------------------------------
    # OPERACIÓN 9 - Segunda reserva correcta
    # -------------------------------------------------
    try:
        reserva2 = Reserva(cliente2, equipo, 5)
        reserva2.confirmar()

        costo = reserva2.procesar()

        print(f"✔ Reserva confirmada. Valor: ${costo}")

        logger.info("Reserva 2 realizada correctamente.")

    except Exception as e:
        logger.error(e)

    # -------------------------------------------------
    # OPERACIÓN 10 - Reserva incorrecta
    # -------------------------------------------------
    try:
        reserva3 = Reserva(cliente2, asesoria, -2)
        reserva3.confirmar()

    except Exception as e:
        logger.error(e)
        print("❌ No se pudo confirmar la reserva.")

    # -------------------------------------------------
    # OPERACIÓN 11 - Servicio inválido
    # -------------------------------------------------
    try:
        ReservaSala("Sala Incorrecta", -500)

    except Exception as e:
        logger.error(e)
        print("❌ Tarifa inválida.")

    # -------------------------------------------------
    # OPERACIÓN 12 - Encadenamiento de excepción
    # -------------------------------------------------
    try:
        try:
            horas = int("ABC")
        except ValueError as error:
            raise Exception(
                "Las horas deben ser numéricas."
            ) from error

    except Exception as e:
        logger.error(e)
        print("❌ Error de conversión.")

    finally:
        logger.info("Simulación finalizada.")

        print("\nSimulación terminada correctamente.")