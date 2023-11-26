from fastapi import APIRouter
import src.routers.raza_routes as razaRoutes
import src.routers.esterilizado_routes as esterilizadoRoutes
import src.routers.microchip_routes as microchipRoutes
import src.routers.localidad_routes as localidadRoutes
import src.routers.estrato_routes as estratoRoutes
import src.routers.nombre_routes as nombreRoutes
import src.routers.fecha_micro_routes as fecha_microRoutes

router = APIRouter()

router.include_router(razaRoutes.raza)
router.include_router(esterilizadoRoutes.esterilizado)
router.include_router(microchipRoutes.microchip)
router.include_router(localidadRoutes.localidad)
router.include_router(estratoRoutes.estrato)
router.include_router(nombreRoutes.nombre)
router.include_router(fecha_microRoutes.fecha_microchip)

