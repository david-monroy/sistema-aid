import conn from "../../api-connector";
import jwt from "../../../common/jwt.service";

export default {
  async obtener(){
    let response = await conn.get(`/sedes/`, jwt.getAuthHeaderToken());
    return response;
  }
};
