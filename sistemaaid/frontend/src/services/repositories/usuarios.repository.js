import conn from "../api-connector";
import jwt from "../../common/jwt.service";

export default {
  async agregar(data){
    let response = await conn.post(`/usuarios/`, data, jwt.getAuthHeaderToken());
    return response;
  },
  async obtener(){
    let response = await conn.get(`/usuarios/`, jwt.getAuthHeaderToken());
    return response;
  },
  async obtenerPorId(id){
    let response = await conn.get(`/usuarios/${id}/`, jwt.getAuthHeaderToken());
    return response;
  },
  async actualizar(id, data){
    let response = await conn.put(`/usuarios/${id}/`, data, jwt.getAuthHeaderToken());
    return response;
  },
  async eliminar(id){
    let response = await conn.delete(`/usuarios/${id}/`, jwt.getAuthHeaderToken());
    return response;
  },
};
