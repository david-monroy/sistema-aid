import conn from "../api-connector";

export default {
  async login(user) {
    let response = await conn.post(`/login`, user);
    return response;
  }
};