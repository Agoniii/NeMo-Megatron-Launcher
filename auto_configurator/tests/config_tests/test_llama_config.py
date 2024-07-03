from omegaconf import OmegaConf


class TestLlamaConfig:
    def test_llama_config_llama3_8b(self):
        conf = OmegaConf.load("conf/search_config/llama/llama3_8b.yaml")
        s = """
        train_settings:
          model_size_in_b: 8 # unit in billion parameters
          num_nodes: 16
          gpus_per_node: 8
          gpu_memory_gb: 80  # Memory per GPU, in GB. Currently 40GB and 80GB A100s supported.
          max_training_days: 6 # unit in days
          limit_search_runs: 100 # Max number of runs to be launched in parallel for grid search.
          output_top_n: 10  # The result will print the top N fastest training configs.
          max_steps_per_run: 50 # Max steps per run for the grid search.
          max_minutes_per_run: 30 # minutes per run for the grid search.
          tflops_per_gpu: 150  # Estimated tflops per GPU.
          num_tokens_in_b: 2400  # Unit in billions, typically 2.4T for llama models.
          vocab_size: 32000
          seq_length: 8192 # available seq_length list for llama models: [2048, 4096, 8192, 16384, 32768]
          custom_config: ${auto_configurator_path}/base_configs/llama3_8b.yaml # path to custom .yaml model config instead of using auto-generated
          logs: ${base_results_dir}/${search_config_value}_${.gpu_memory_gb}gb  # Example base_results_dir/gpt3/126m
          tensor_parallel_sizes: auto  # auto to use our recommendation, or a list, such as [1, 2, 4, 8]
          pipeline_parallel_sizes: auto  # auto to use our recommendation, or a list, such as [1, 2, 4, 8, 10]
          context_parallel_sizes: [1, 2] # a list, such as [1, 2, 4], auto is not supported yet
          min_model_parallel_size: auto  # auto to use our recommendation, or a value for the minimum desired parallelism
          max_model_parallel_size: auto  # auto to use our recommendation, or a value for the maximum desired parallelism
          micro_batch_sizes: auto  # auto to use our recommendation, or a list, such as [1, 2, 4, 8, 16]
          act_ckpt_layers: auto  # auto to use our recommendation, or a list, such as [0, 1, 2, 3]
        """
        expected = OmegaConf.create(s)
        assert (
            expected == conf
        ), f"conf/search_config/llama/llama3_8b.yaml must be set to {expected} but it currently is {conf}."

    def test_llama_config_llama3_70b(self):
        conf = OmegaConf.load("conf/search_config/llama/llama3_70b.yaml")
        s = """
        train_settings:
          model_size_in_b: 70 # unit in billion parameters
          num_nodes: 128
          gpus_per_node: 8
          gpu_memory_gb: 80  # Memory per GPU, in GB. Currently 40GB and 80GB A100s supported.
          max_training_days: 12 # unit in days
          limit_search_runs: 100 # Max number of runs to be launched in parallel for grid search.
          output_top_n: 10  # The result will print the top N fastest training configs.
          max_steps_per_run: 50 # Max steps per run for the grid search.
          max_minutes_per_run: 30 # minutes per run for the grid search.
          tflops_per_gpu: 150  # Estimated tflops per GPU.
          num_tokens_in_b: 2400  # Unit in billions, typically 2.4T for llama models.
          vocab_size: 32000
          seq_length: 8192 # available seq_length list for llama models: [2048, 4096, 8192, 16384, 32768]
          custom_config: ${auto_configurator_path}/base_configs/llama3_70b.yaml # path to custom .yaml model config instead of using auto-generated
          logs: ${base_results_dir}/${search_config_value}_${.gpu_memory_gb}gb  # Example base_results_dir/gpt3/126m
          tensor_parallel_sizes: auto  # auto to use our recommendation, or a list, such as [1, 2, 4, 8]
          pipeline_parallel_sizes: auto  # auto to use our recommendation, or a list, such as [1, 2, 4, 8, 10]
          context_parallel_sizes: [1, 2, 4] # a list, such as [1, 2, 4], auto is not supported yet
          min_model_parallel_size: auto  # auto to use our recommendation, or a value for the minimum desired parallelism
          max_model_parallel_size: auto  # auto to use our recommendation, or a value for the maximum desired parallelism
          micro_batch_sizes: auto  # auto to use our recommendation, or a list, such as [1, 2, 4, 8, 16]
          act_ckpt_layers: auto  # auto to use our recommendation, or a list, such as [0, 1, 2, 3]
        """
        expected = OmegaConf.create(s)
        assert (
            expected == conf
        ), f"conf/search_config/llama/llama3_70b.yaml must be set to {expected} but it currently is {conf}."

    def test_llama_config_llama2_7b(self):
        conf = OmegaConf.load("conf/search_config/llama/llama2_7b.yaml")
        s = """
        train_settings:
          model_size_in_b: 7 # unit in billion parameters
          num_nodes: 1
          gpus_per_node: 8
          gpu_memory_gb: 80  # Memory per GPU, in GB. Currently 40GB and 80GB A100s supported.
          max_training_days: 5 # unit in days
          limit_search_runs: 100 # Max number of runs to be launched in parallel for grid search.
          output_top_n: 10  # The result will print the top N fastest training configs.
          max_steps_per_run: 100 # Max steps per run for the grid search.
          max_minutes_per_run: 30 # minutes per run for the grid search.
          tflops_per_gpu: 150  # Estimated tflops per GPU.
          num_tokens_in_b: 300  # Unit in billions, typically 300B for GPT3 models.
          vocab_size: 32000
          seq_length: 4096 # available seq_length list for GPT-3 models: [2048, 4096, 8192, 16384, 32768]
          custom_config: ${auto_configurator_path}/base_configs/llama2_7b.yaml # path to custom .yaml model config instead of using auto-generated
          logs: ${base_results_dir}/${search_config_value}_${.gpu_memory_gb}gb  # Example base_results_dir/gpt3/126m
          tensor_parallel_sizes: auto  # auto to use our recommendation, or a list, such as [1, 2, 4, 8]
          pipeline_parallel_sizes: auto  # auto to use our recommendation, or a list, such as [1, 2, 4, 8, 10]
          min_model_parallel_size: auto  # auto to use our recommendation, or a value for the minimum desired parallelism
          max_model_parallel_size: auto  # auto to use our recommendation, or a value for the maximum desired parallelism
          micro_batch_sizes: auto  # auto to use our recommendation, or a list, such as [1, 2, 4, 8, 16]
          act_ckpt_layers: auto  # auto to use our recommendation, or a list, such as [0, 1, 2, 3]
        """
        expected = OmegaConf.create(s)
        assert (
            expected == conf
        ), f"conf/search_config/llama/llama2_7b.yaml must be set to {expected} but it currently is {conf}."
      
    def test_llama_config_llama2_13b(self):
        conf = OmegaConf.load("conf/search_config/llama/llama2_13b.yaml")
        s = """
        train_settings:
          model_size_in_b: 13 # unit in billion parameters
          num_nodes: 2
          gpus_per_node: 8
          gpu_memory_gb: 80  # Memory per GPU, in GB. Currently 40GB and 80GB A100s supported.
          max_training_days: 5 # unit in days
          limit_search_runs: 100 # Max number of runs to be launched in parallel for grid search.
          output_top_n: 10  # The result will print the top N fastest training configs.
          max_steps_per_run: 100 # Max steps per run for the grid search.
          max_minutes_per_run: 30 # minutes per run for the grid search.
          tflops_per_gpu: 150  # Estimated tflops per GPU.
          num_tokens_in_b: 300  # Unit in billions, typically 300B for GPT3 models.
          vocab_size: 32000
          seq_length: 4096 # available seq_length list for GPT-3 models: [2048, 4096, 8192, 16384, 32768]
          custom_config: ${auto_configurator_path}/base_configs/llama2_13b.yaml # path to custom .yaml model config instead of using auto-generated
          logs: ${base_results_dir}/${search_config_value}_${.gpu_memory_gb}gb  # Example base_results_dir/gpt3/126m
          tensor_parallel_sizes: auto  # auto to use our recommendation, or a list, such as [1, 2, 4, 8]
          pipeline_parallel_sizes: auto  # auto to use our recommendation, or a list, such as [1, 2, 4, 8, 10]
          min_model_parallel_size: auto  # auto to use our recommendation, or a value for the minimum desired parallelism
          max_model_parallel_size: auto  # auto to use our recommendation, or a value for the maximum desired parallelism
          micro_batch_sizes: auto  # auto to use our recommendation, or a list, such as [1, 2, 4, 8, 16]
          act_ckpt_layers: auto  # auto to use our recommendation, or a list, such as [0, 1, 2, 3]
        """
        expected = OmegaConf.create(s)
        assert (
            expected == conf
        ), f"conf/search_config/llama/llama2_13b.yaml must be set to {expected} but it currently is {conf}."

    def test_llama_config_llama2_70b(self):
        conf = OmegaConf.load("conf/search_config/llama/llama2_70b.yaml")
        s = """
        train_settings:
          model_size_in_b: 70 # unit in billion parameters
          num_nodes: 8
          gpus_per_node: 8
          gpu_memory_gb: 80  # Memory per GPU, in GB. Currently 40GB and 80GB A100s supported.
          max_training_days: 5 # unit in days
          limit_search_runs: 100 # Max number of runs to be launched in parallel for grid search.
          output_top_n: 10  # The result will print the top N fastest training configs.
          max_steps_per_run: 100 # Max steps per run for the grid search.
          max_minutes_per_run: 30 # minutes per run for the grid search.
          tflops_per_gpu: 150  # Estimated tflops per GPU.
          num_tokens_in_b: 300  # Unit in billions, typically 300B for GPT3 models.
          vocab_size: 32000
          seq_length: 4096 # available seq_length list for GPT-3 models: [2048, 4096, 8192, 16384, 32768]
          custom_config: ${auto_configurator_path}/base_configs/llama2_70b.yaml # path to custom .yaml model config instead of using auto-generated
          logs: ${base_results_dir}/${search_config_value}_${.gpu_memory_gb}gb  # Example base_results_dir/gpt3/126m
          tensor_parallel_sizes: auto  # auto to use our recommendation, or a list, such as [1, 2, 4, 8]
          pipeline_parallel_sizes: auto  # auto to use our recommendation, or a list, such as [1, 2, 4, 8, 10]
          min_model_parallel_size: auto  # auto to use our recommendation, or a value for the minimum desired parallelism
          max_model_parallel_size: auto  # auto to use our recommendation, or a value for the maximum desired parallelism
          micro_batch_sizes: auto  # auto to use our recommendation, or a list, such as [1, 2, 4, 8, 16]
          act_ckpt_layers: auto  # auto to use our recommendation, or a list, such as [0, 1, 2, 3]
        """
        expected = OmegaConf.create(s)
        assert (
            expected == conf
        ), f"conf/search_config/llama/llama2_70b.yaml must be set to {expected} but it currently is {conf}."
