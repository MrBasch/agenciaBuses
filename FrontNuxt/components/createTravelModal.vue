<template>
  <v-dialog max-width="500px" v-model="open">
    <v-card class="addDialog">
      <v-card-title class="cardTitle">Add Travel</v-card-title>
      <v-form>
        <v-text-field v-model="code" label="Enter travel code"></v-text-field>
        <v-text-field
          v-model="start_time"
          label="Enter travel start time"
          placeholder="2022-02-04 11:30:45"
        ></v-text-field>
        <v-text-field
          v-model="end_time"
          label="Enter travel end time"
          placeholder="2022-02-05 12:30:45"
        ></v-text-field>
        <v-select
          v-model="rut_driver"
          :items="drivers_rut"
          label="Select a driver"
        ></v-select>
        <v-select
          v-model="code_bus"
          :items="buses"
          label="Select a bus"
        ></v-select>
        <v-select
          v-model="code_route"
          :items="routes"
          label="Select a route"
        ></v-select>
      </v-form>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          @click.stop="
            saveTravel(
              (code = code),
              (code_route = code_route),
              (start_time = start_time),
              (end_time = end_time),
              (rut_driver = rut_driver),
              (code_bus = code_bus)
            )
          "
          color="#417D7A"
          >Add</v-btn
        >
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
export default {
  name: "createTravelModal",
  props: ["open"],
  data() {
    return {
      code: "",
      state: "",
      start_time: "",
      end_time: "",
      rut_driver: "",
      code_bus: "",
      code_route: "",
      drivers: [],
      drivers_rut: [],
      buses: [],
      routes: [],
    };
  },
  methods: {
    async saveTravel(
      code,
      code_route,
      start_time,
      end_time,
      rut_driver,
      code_bus
    ) {
      const selected_driver = this.drivers.filter(
        (driver) => driver.rut === rut_driver
      );
      await fetch(
        `http://127.0.0.1:8000/back/travel?code=${code}&route=${code_route}&start_time=${start_time}&end_time=${end_time}&driver=${selected_driver[0].rut}&bus=${code_bus}`,
        {
          method: "POST",
          mode: "cors",
          headers: {
            Authorization: `Token ${localStorage.token}`,
          },
          cache: "default",
        }
      ).then((res) =>
        res.json().then((data) => {
          console.log(data);
        })
      );
    },
    async getBuses() {
      await fetch("http://127.0.0.1:8000/back/bus", {
        method: "GET",
        mode: "cors",
        headers: {
          Authorization: `Token ${localStorage.token}`,
        },
        cache: "default",
      }).then((res) =>
        res.json().then((data) => {
          data.map((bus) => this.buses.push(bus.code));
        })
      );
    },
    async getDrivers() {
      await fetch("http://127.0.0.1:8000/back/driver", {
        method: "GET",
        mode: "cors",
        headers: {
          Authorization: `Token ${localStorage.token}`,
        },
        cache: "default",
      }).then((res) =>
        res.json().then((data) => {
          data.map((driver) => {
            this.drivers.push(driver);
            this.drivers_rut.push(driver.rut);
          });
        })
      );
    },
    async getRoutes() {
      await fetch("http://127.0.0.1:8000/back/route", {
        method: "GET",
        mode: "cors",
        headers: {
          Authorization: `Token ${localStorage.token}`,
        },
        cache: "default",
      }).then((res) =>
        res.json().then((data) => {
          data.map((route) => this.routes.push(route.code));
        })
      );
    },
  },
  created() {
    this.getBuses();
    this.getDrivers();
    this.getRoutes();
  },
};
</script>
<style scoped>
.addDialog {
  overflow: hidden;
  background-color: #8b8070;
}
</style>