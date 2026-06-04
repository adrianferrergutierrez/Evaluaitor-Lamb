#!/usr/bin/env python3
"""
test_scenario4.py - Test de l'Escenari 4: Continuació de Sessió
"""

from dotenv import load_dotenv
load_dotenv()

from core.tool_registry import registry
from core.agent.agent import Agent
import json

print('🧪 Escenari 4: Continuació de Sessió')
print('=' * 60)

# Pas 1: Executar workflow directament (sense agent)
print('\n📝 Pas 1: Executar workflow directament')
print('-' * 60)

result = registry.execute(
    'execute_workflow',
    workflow_path='workflows/hito2_no_vision.json',
    input_doc='tests/test-1-hito-2/A1.1 Memoria trabajo final (2).docx',
    output_dir='results/hito2_scenario4',
    rubric_path='configs/rubric_hito2.yaml'
)

print(f'✅ Workflow executat')
print(f'Status: {result["result"]["status"]}')
print(f'Log: {result["result"]["log_path"]}')

# Llegir les puntuacions
with open('results/hito2_scenario4/eval/scores.json') as f:
    scores = json.load(f)

print(f'\n📊 Puntuacions inicials:')
for criterion, score in scores['scores'].items():
    print(f'  - {criterion}: {score}/10')

# Pas 2: Crear agent i continuar sessió amb canvi
print('\n📝 Pas 2: Continuar sessió amb canvi')
print('-' * 60)

agent = Agent()

# Segona crida: canviar puntuació d'un criteri
response, session_id = agent.run(
    f'Canvia la puntuació del criteri "Memoria técnica" a 9.0/10 i recalcula la nota final. Les puntuacions actuals són: {json.dumps(scores["scores"])}'
)

print(f'\n✅ Segona crida completada')
print(f'Session ID: {session_id}')
print(f'Response:\n{response}')
