import { foldDeviceEvents } from "./fold-device-events.mjs";

export function materializeDevices(batch) {
  return foldDeviceEvents(batch.events);
}
