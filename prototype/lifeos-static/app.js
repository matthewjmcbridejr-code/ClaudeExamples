const members = [
  { name: 'Parent Admin', role: 'Owner', initials: 'PA' },
  { name: 'Adult Member', role: 'Tasks + calendar', initials: 'AM' },
  { name: 'Child Member', role: 'Assigned tasks', initials: 'CM' },
  { name: 'Helper', role: 'Limited access', initials: 'H' }
];

const tasks = [
  { title: 'Take recycling out', owner: 'Adult Member', status: 'Due today' },
  { title: 'Pack school bag', owner: 'Child Member', status: 'Waiting' },
  { title: 'Confirm grocery pickup', owner: 'Parent Admin', status: 'Done' },
  { title: 'Reset kitchen display', owner: 'Helper', status: 'Due today' }
];

const calendar = [
  { time: '8:30 AM', title: 'School drop-off', detail: 'Display-safe' },
  { time: '12:15 PM', title: 'Grocery pickup', detail: 'Assigned to Parent Admin' },
  { time: '6:00 PM', title: 'Family dinner', detail: 'Shared event' }
];

const assets = [
  { item: 'Family car', slot: '3:00 PM - 5:00 PM', owner: 'Adult Member' },
  { item: 'Guest room', slot: 'Friday', owner: 'Parent Admin' },
  { item: 'Projector', slot: 'Available tonight', owner: 'Shared' }
];

function badgeClass(status) {
  if (status === 'Done') return 'badge done';
  if (status === 'Waiting') return 'badge waiting';
  return 'badge';
}

function renderMembers() {
  document.querySelector('#members').innerHTML = members.map(member => `
    <article class="member">
      <div class="avatar">${member.initials}</div>
      <strong>${member.name}</strong>
      <span>${member.role}</span>
    </article>
  `).join('');
}

function renderTasks() {
  document.querySelector('#task-count').textContent = `${tasks.length} items`;
  document.querySelector('#tasks').innerHTML = tasks.map(task => `
    <article class="task">
      <div>
        <strong>${task.title}</strong>
        <span>Owner: ${task.owner}</span>
      </div>
      <span class="${badgeClass(task.status)}">${task.status}</span>
    </article>
  `).join('');
}

function renderCalendar() {
  document.querySelector('#calendar').innerHTML = calendar.map(item => `
    <article class="item">
      <strong>${item.time} · ${item.title}</strong>
      <span>${item.detail}</span>
    </article>
  `).join('');
}

function renderAssets() {
  document.querySelector('#assets').innerHTML = assets.map(asset => `
    <article class="item">
      <strong>${asset.item}</strong>
      <span>${asset.slot} · ${asset.owner}</span>
    </article>
  `).join('');
}

function renderDisplay() {
  const today = new Date();
  document.querySelector('#display-date').textContent = today.toLocaleDateString(undefined, {
    weekday: 'short', month: 'short', day: 'numeric'
  });

  const dueTasks = tasks.filter(task => task.status !== 'Done').slice(0, 3);
  const nextEvents = calendar.slice(0, 3);
  const bookings = assets.slice(0, 2);

  document.querySelector('#epaper-summary').innerHTML = `
    <section class="display-card">
      <h3>Tasks</h3>
      ${dueTasks.map(task => `<p>${task.title}<br>${task.owner}</p>`).join('')}
    </section>
    <section class="display-card">
      <h3>Calendar</h3>
      ${nextEvents.map(item => `<p>${item.time}<br>${item.title}</p>`).join('')}
    </section>
    <section class="display-card">
      <h3>Assets</h3>
      ${bookings.map(asset => `<p>${asset.item}<br>${asset.slot}</p>`).join('')}
    </section>
  `;
}

renderMembers();
renderTasks();
renderCalendar();
renderAssets();
renderDisplay();
