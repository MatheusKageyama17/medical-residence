import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace tabs with select
tabs_html = """  <div class="simulator-tabs">
    <button class="sim-tab active" id="tab-TResidence" onclick="switchSimulator('TResidence')">TResidence</button>
    <button class="sim-tab" id="tab-CBMC" onclick="switchSimulator('CBMC')">CBMC</button>
  </div>"""

select_html = """  <div class="simulator-selector" style="margin-top: 15px; text-align: center;">
    <label for="simSelector" style="color: #fff; font-weight: bold; margin-right: 10px;">Selecione o Empreendimento:</label>
    <select id="simSelector" onchange="switchSimulator(this.value)" style="padding: 10px; border-radius: 5px; border: 1px solid #ccc; font-size: 16px; min-width: 200px;">
      <option value="TResidence">TIMELESS RESIDENCE</option>
      <option value="CBMC">MEDICAL CBMC</option>
    </select>
  </div>"""

html = html.replace(tabs_html, select_html)

# Clean up switchSimulator (remove tab classes logic)
old_switch = """function switchSimulator(sim) {
  currentSimulator = sim;
  document.querySelectorAll('.sim-tab').forEach(el => el.classList.remove('active'));
  document.getElementById('tab-' + sim).classList.add('active');"""

new_switch = """function switchSimulator(sim) {
  try {
  currentSimulator = sim;
  console.log("Switching to", sim);"""

html = html.replace(old_switch, new_switch)

# Add catch to switchSimulator
old_switch_end = """  // clear live bar
  document.getElementById('liveTotalBar').classList.remove('visible');
}"""

new_switch_end = """  // clear live bar
  const liveTotalBar = document.getElementById('liveTotalBar');
  if (liveTotalBar) liveTotalBar.classList.remove('visible');
  } catch (err) { console.error("Error in switchSimulator:", err); }
}"""

html = html.replace(old_switch_end, new_switch_end)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html updated with select dropdown and try-catch.")
