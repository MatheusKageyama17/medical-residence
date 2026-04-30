import re
import json

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('cbmc_units.json', 'r', encoding='utf-8') as f:
    cbmc_units = f.read()

# Add styles for the dropdown
style_addition = """
    /* Tab / Simulator Selector Styles */
    .simulator-tabs {
      display: flex;
      justify-content: center;
      gap: 10px;
      margin-bottom: 20px;
      margin-top: -10px;
    }
    .sim-tab {
      padding: 10px 20px;
      border: 2px solid rgba(255, 255, 255, 0.4);
      border-radius: 8px;
      background: rgba(255, 255, 255, 0.1);
      color: white;
      font-weight: 700;
      font-size: 16px;
      cursor: pointer;
      transition: all 0.3s;
    }
    .sim-tab:hover {
      background: rgba(255, 255, 255, 0.3);
    }
    .sim-tab.active {
      background: white;
      color: var(--primary);
      border-color: white;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    }
"""

html = html.replace('</style>', style_addition + '\n</style>')

# Add the tabs to the header area, below the title
header_addition = """
  </div>
  <div class="simulator-tabs">
    <button class="sim-tab active" id="tab-TResidence" onclick="switchSimulator('TResidence')">TResidence</button>
    <button class="sim-tab" id="tab-CBMC" onclick="switchSimulator('CBMC')">CBMC</button>
  </div>
</header>
"""

# The current header has <div><h1>Simulador de Compra</h1><p>TIMELESS RESIDENCE</p></div></header>
# But wait, looking at the previous view_file, we didn't see the closing </header> yet because it was cut off. Let's just find </header> and insert before it.

# Let's replace the fixed title with a dynamic one
html = re.sub(r'<div>\s*<h1>Simulador de Compra</h1>\s*<p>TIMELESS RESIDENCE</p>\s*</div>', 
              r'''<div style="text-align: center;">
    <h1 id="mainTitle">Simulador de Compra</h1>
    <p id="mainSubtitle" style="font-size: 16px; margin-top: 5px; opacity: 0.9; font-weight: 600;">TIMELESS RESIDENCE</p>
  </div>''', html)

html = html.replace('</header>', '''
  <div class="simulator-tabs">
    <button class="sim-tab active" id="tab-TResidence" onclick="switchSimulator('TResidence')">TResidence</button>
    <button class="sim-tab" id="tab-CBMC" onclick="switchSimulator('CBMC')">CBMC</button>
  </div>
</header>''')

# Now for the JS part
# Replace `const UNITS = [` with `const UNITS_TRESIDENCE = [`
html = html.replace('const UNITS = [', 'const UNITS_TRESIDENCE = [')

# Add UNITS_CBMC and the simulator switching logic before `const fmt = v =>`
cbmc_units_declaration = f"const UNITS_CBMC = {cbmc_units};\n"
cbmc_units_declaration += "let currentSimulator = 'TResidence';\n"
cbmc_units_declaration += "let UNITS = UNITS_TRESIDENCE;\n\n"
cbmc_units_declaration += """
function switchSimulator(sim) {
  currentSimulator = sim;
  document.querySelectorAll('.sim-tab').forEach(el => el.classList.remove('active'));
  document.getElementById('tab-' + sim).classList.add('active');
  
  if (sim === 'TResidence') {
    UNITS = UNITS_TRESIDENCE;
    document.getElementById('mainSubtitle').textContent = 'TIMELESS RESIDENCE';
  } else if (sim === 'CBMC') {
    UNITS = UNITS_CBMC;
    document.getElementById('mainSubtitle').textContent = 'MEDICAL CBMC';
  }
  
  // Reset UI
  const selAndar = document.getElementById('selAndar');
  selAndar.innerHTML = '<option value="">— Selecione o andar —</option>';
  const floors = [...new Set(UNITS.map(u => u.andar))].sort((a,b) => +a - +b);
  floors.forEach(f => {
    const opt = document.createElement('option');
    opt.value = f;
    opt.text = `${f}º Andar`;
    selAndar.appendChild(opt);
  });
  
  const selU = document.getElementById('selUnidade');
  selU.innerHTML = '<option value="">— Selecione a unidade —</option>';
  selU.disabled = true;
  document.getElementById('unitInfo').classList.remove('visible');
  document.getElementById('summaryBar').classList.remove('visible');
  document.getElementById('resultSection').classList.remove('visible');
  
  // Clear proposed units
  _proposalUnits = [];
  renderUnitList();
  document.getElementById('unitListSection').classList.remove('visible');
  document.getElementById('consolidatedSummary').style.display='none';
  document.getElementById('consolidatedPrint').style.display='none';
  
  // clear live bar
  document.getElementById('liveTotalBar').classList.remove('visible');
}
"""

html = html.replace("const fmt = v =>", cbmc_units_declaration + "const fmt = v =>")

with open('index_updated.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML successfully modified.")
