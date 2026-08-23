export function foldDeviceEvents(events) {
  const devices = new Map();
  for (const event of events) {
    if (event.kind === "snapshot") devices.set(event.deviceId, { sequence: event.sequence, state: { ...event.state } });
    else if (event.kind === "patch") {
      const device = devices.get(event.deviceId);
      Object.assign(device.state, event.changes);
      device.sequence = event.sequence;
    }
    else if (event.kind === "delete") devices.delete(event.deviceId);
  }
  return [...devices].map(([deviceId, device]) => ({ deviceId, sequence: device.sequence, state: device.state }));
}
