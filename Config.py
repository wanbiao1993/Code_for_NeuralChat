import Prompts

cfg_tabletop = {
  'lmps': {
    'tabletop_ui': {
      'prompt_text': Prompts.prompt_tabletop_ui,
      # 'engine': 'text-davinci-003',
      # 'engine': 'Mixtral-8x7B-Instruct-v0.1',
        'engine':'Mixtral-8x7B-Instruct-v0.1',
      'max_tokens': 512,
      'temperature': 0.0000000000001,
      'query_prefix': '# ',
      'query_suffix': '.',
      'stop': ['#', 'objects = ['],
      'maintain_session': True,
      'debug_mode': False,
      'include_context': True,
      'has_return': False,
      'return_val_name': 'ret_val',
    },
    'parse_obj_name': {
      'prompt_text': Prompts.prompt_parse_obj_name,
      # 'engine': 'text-davinci-003',
      # 'engine': 'Mixtral-8x7B-Instruct-v0.1',
        'engine':'Mixtral-8x7B-Instruct-v0.1',
      'max_tokens': 512,
      'temperature': 0.0000000000001,
      'query_prefix': '# ',
      'query_suffix': '.',
      'stop': ['#', 'objects = ['],
      'maintain_session': False,
      'debug_mode': False,
      'include_context': True,
      'has_return': True,
      'return_val_name': 'ret_val',
    },
    'parse_position': {
      'prompt_text': Prompts.prompt_parse_position,
      # 'engine': 'text-davinci-003',
        # 'engine': 'Mixtral-8x7B-Instruct-v0.1',
        'engine':'Mixtral-8x7B-Instruct-v0.1',
      'max_tokens': 512,
      'temperature': 0.0000000000001,
      'query_prefix': '# ',
      'query_suffix': '.',
      'stop': ['#'],
      'maintain_session': False,
      'debug_mode': False,
      'include_context': True,
      'has_return': True,
      'return_val_name': 'ret_val',
    },
    'parse_question': {
      'prompt_text': Prompts.prompt_parse_question,
      # 'engine': 'text-davinci-003',
        # 'engine': 'Mixtral-8x7B-Instruct-v0.1',
        'engine':'Mixtral-8x7B-Instruct-v0.1',
      'max_tokens': 512,
      'temperature': 0.0000000000001,
      'query_prefix': '# ',
      'query_suffix': '.',
      'stop': ['#', 'objects = ['],
      'maintain_session': False,
      'debug_mode': False,
      'include_context': True,
      'has_return': True,
      'return_val_name': 'ret_val',
    },
    'transform_shape_pts': {
      'prompt_text': Prompts.prompt_transform_shape_pts,
      # 'engine': 'text-davinci-003',
        # 'engine': 'Mixtral-8x7B-Instruct-v0.1',
        'engine':'Mixtral-8x7B-Instruct-v0.1',
      'max_tokens': 512,
      'temperature': 0.0000000000001,
      'query_prefix': '# ',
      'query_suffix': '.',
      'stop': ['#'],
      'maintain_session': False,
      'debug_mode': False,
      'include_context': True,
      'has_return': True,
      'return_val_name': 'new_shape_pts',
    },
    'fgen': {
      'prompt_text': Prompts.prompt_fgen,
      # 'engine': 'text-davinci-003',
        # 'engine': 'Mixtral-8x7B-Instruct-v0.1',
        'engine':'Mixtral-8x7B-Instruct-v0.1',
      'max_tokens': 512,
      'temperature': 0.0000000000001,
      'query_prefix': '# define function: ',
      'query_suffix': '.',
      'stop': ['# define', '# example'],
      'maintain_session': False,
      'debug_mode': False,
      'include_context': True,
    }
  }
}

lmp_tabletop_coords = {
        'top_left':     (-0.3 + 0.05, -0.2 - 0.05),
        'top_side':     (0,           -0.2 - 0.05),
        'top_right':    (0.3 - 0.05,  -0.2 - 0.05),
        'left_side':    (-0.3 + 0.05, -0.5,      ),
        'middle':       (0,           -0.5,      ),
        'right_side':   (0.3 - 0.05,  -0.5,      ),
        'bottom_left':  (-0.3 + 0.05, -0.8 + 0.05),
        'bottom_side':  (0,           -0.8 + 0.05),
        'bottom_right': (0.3 - 0.05,  -0.8 + 0.05),
        'table_z':       0.0,
      }